from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crypto_engine.protocols import DiffieHellmanProtocol
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Simulation State
STATE = {
    "arda": None,
    "burak": None,
    "mallory_active": False,
    "messages": []
}


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('init_handshake')
def handle_handshake(data):
    """Scenario: Normal DH Handshake"""
    scenario_type = data.get('type')  # 'static' or 'ephemeral'

    # 1. arda Generates Key
    STATE['arda'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    emit('log', {'source': 'arda', 'msg': f'Generated Private Key: {str(STATE["arda"]._private_key)[:6]}...'})
    emit('anim_key_gen', {'target': 'arda'})

    # 2. burak Generates Key (Static or New)
    if scenario_type == 'static' and STATE['burak']:
        emit('log', {'source': 'burak', 'msg': 'Using STATIC Private Key (No Refresh)'})
    else:
        STATE['burak'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
        emit('log', {'source': 'burak', 'msg': f'Generated Ephemeral Key: {str(STATE["burak"]._private_key)[:6]}...'})
        emit('anim_key_gen', {'target': 'burak'})

    # 3. Public Key Exchange Animation
    emit('anim_packet', {
        'from': 'arda', 'to': 'burak',
        'payload': f'PubA: {str(STATE["arda"].public_key)[:10]}...',
        'intercepted': STATE['mallory_active']
    })


@socketio.on('complete_handshake')
def finalize_handshake():
    """Calculates shared secrets after animation finishes"""
    if STATE['mallory_active']:
        # ATTACK: Subgroup Confinement
        # Mallory injects P-1
        p_minus_1 = DH_2048_P - 1

        # burak computes secret using P-1
        # In a real library this raises an error, here we force it for demo
        # burak's Secret = (P-1)^b mod P
        burak_secret = pow(p_minus_1, STATE['burak']._private_key, DH_2048_P)

        emit('log', {'source': 'Mallory', 'msg': 'ATTACK: Injected (P-1) as Public Key!'})
        emit('log', {'source': 'burak', 'msg': 'Computed Shared Secret (CORRUPTED)'})
        emit('update_status', {'actor': 'burak', 'status': 'compromised', 'secret': str(burak_secret)})
        emit('update_status', {'actor': 'mallory', 'status': 'cracked', 'secret': '1 or P-1'})

    else:
        # Normal DH
        arda_s = STATE['arda'].generate_shared_secret(STATE['burak'].public_key)
        burak_s = STATE['burak'].generate_shared_secret(STATE['arda'].public_key)

        emit('log', {'source': 'System', 'msg': 'Handshake Secure. Channel Established.'})
        emit('update_status', {'actor': 'arda', 'status': 'secure', 'secret': str(arda_s)[:10]})
        emit('update_status', {'actor': 'burak', 'status': 'secure', 'secret': str(burak_s)[:10]})


@socketio.on('toggle_attack')
def toggle_attack():
    STATE['mallory_active'] = not STATE['mallory_active']
    status = "ACTIVE" if STATE['mallory_active'] else "IDLE"
    emit('log', {'source': 'Mallory', 'msg': f'Interception Mode: {status}'})
    emit('update_mallory', {'active': STATE['mallory_active']})


@socketio.on('leak_key')
def leak_key():
    """Forward Secrecy Demo: Leak burak's Key"""
    if not STATE['burak']: return
    key = str(STATE['burak']._private_key)
    emit('log', {'source': 'System', 'msg': f'CRITICAL: burak\'s Key LEAKED: {key[:10]}...'})
    emit('anim_leak', {'key': key})


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)