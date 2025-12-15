from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import sys
import os
import uuid
import hashlib
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crypto_engine.protocols import DiffieHellmanProtocol
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# State Management
STATE = {
    "arda": None,
    "burak": None,
    "mallory_intercept_mode": False,
    "current_session_id": None,
    "shared_secrets": {"arda": None, "burak": None, "mallory": None},
    "history": []  # {id, time, type, compromised}
}


def derive_key(secret_int):
    """Derive a simple AES-like key from the integer secret."""
    if secret_int is None: return None
    return hashlib.sha256(str(secret_int).encode()).hexdigest()[:16]  # 16 chars


def xor_encrypt(msg, secret):
    """Toy encryption for visualization."""
    if secret is None: return msg
    key = derive_key(secret)
    encrypted = []
    for i, char in enumerate(msg):
        key_char = key[i % len(key)]
        encrypted.append(chr(ord(char) ^ ord(key_char)))
    return ''.join(encrypted)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('init_handshake')
def handle_handshake(data):
    STATE['current_session_id'] = str(uuid.uuid4())[:6]
    STATE['shared_secrets'] = {"arda": None, "burak": None, "mallory": None}

    # 1. Init Arda (Always Ephemeral)
    STATE['arda'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)

    # 2. Init Burak (Static or Ephemeral)
    if data['type'] == 'static' and STATE['burak']:
        pass  # Keep existing key
    else:
        STATE['burak'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)

    emit('log', {'source': 'Sistem', 'msg': 'El sıkışma başlatıldı.'})
    emit('narrate', {'text': 'Arda Açık Anahtarını (Public Key) Burak\'a gönderiyor...'})

    # 3. Animate Packet (Checks if interception is on)
    emit('anim_packet_start', {
        'intercept_mode': STATE['mallory_intercept_mode'],
        'original_payload': str(STATE['arda'].public_key)[:12] + '...'
    })


@socketio.on('packet_forwarded')
def handle_forward(data):
    """Called after user manually forwards packet from modal."""
    injection_type = data.get('inject_type')

    payload_to_burak = STATE['arda'].public_key

    if injection_type == 'subgroup':
        payload_to_burak = DH_2048_P - 1  # Malicious P-1
        STATE['shared_secrets']['mallory'] = 'DETECTED'  # Flag
        emit('log', {'source': 'Mallory', 'msg': 'ENJEKSİYON: (P-1) değeri gönderildi.'})
        emit('narrate', {'text': 'Mallory paketi değiştirdi! Alt Grup Saldırısı yapılıyor.'})
    elif injection_type == 'random':
        payload_to_burak = 123456789  # Junk
        emit('log', {'source': 'Mallory', 'msg': 'Bozuk veri gönderildi.'})
    else:
        emit('log', {'source': 'Mallory', 'msg': 'Paket değiştirilmeden iletildi.'})
        emit('narrate', {'text': 'Mallory sadece izliyor. Paket değiştirilmedi.'})

    # Complete the animation to Burak
    emit('anim_packet_end', {'success': True})

    # Calculate Secrets
    try:
        # Burak computes based on what he received
        burak_secret = pow(payload_to_burak, STATE['burak']._private_key, DH_2048_P)
        STATE['shared_secrets']['burak'] = burak_secret

        # Arda computes normally (assuming he got Burak's key correctly for this simplified demo)
        arda_secret = STATE['arda'].generate_shared_secret(STATE['burak'].public_key)
        STATE['shared_secrets']['arda'] = arda_secret

        # Check security status
        is_secure = (burak_secret == arda_secret) and (injection_type == 'original')

        # Add to history
        sess_entry = {
            'id': STATE['current_session_id'],
            'time': datetime.now().strftime("%H:%M:%S"),
            'burak_priv_ref': STATE['burak']._private_key,
            'is_compromised': False  # Will change if key leaks
        }
        if not is_secure: sess_entry['is_compromised'] = True  # Immediately broken if MitM

        STATE['history'].insert(0, sess_entry)
        if len(STATE['history']) > 8: STATE['history'].pop()

        emit('update_history', STATE['history'])
        emit('handshake_complete', {'secure': is_secure})

    except Exception as e:
        print(e)


@socketio.on('send_chat')
def handle_chat(data):
    """Encrypts message with calculated keys."""
    msg = data['msg']

    # Arda encrypts
    cipher = xor_encrypt(msg, STATE['shared_secrets']['arda'])

    # Send visualization
    emit('anim_chat', {'cipher': cipher[:10] + '...'})

    # Burak decrypts
    try:
        decrypted = xor_encrypt(cipher, STATE['shared_secrets']['burak'])
    except:
        decrypted = "????"

    # Check validity (simple check)
    success = (decrypted == msg)

    emit('chat_delivery', {
        'original': msg,
        'cipher': cipher,  # In real app, hex encode this
        'decrypted': decrypted,
        'success': success
    })

    # If Mallory did Subgroup attack, show she can read it
    if STATE['shared_secrets']['mallory'] == 'DETECTED':
        # Mallory tries keys 1 and P-1.
        # For demo, if MitM was active, we assume she cracked it.
        emit('log', {'source': 'Mallory', 'msg': f'Mesaj Çözüldü: "{msg}"'})


@socketio.on('toggle_interception')
def toggle(data):
    STATE['mallory_intercept_mode'] = data['active']
    msg = "Aktif (Paketleri Durduracak)" if data['active'] else "Pasif"
    emit('narrate', {'text': f'Mallory Müdahale Modu: {msg}'})
    emit('mallory_state', {'active': data['active']})


@socketio.on('leak_key')
def leak_key():
    if not STATE['burak']: return
    leaked_key = STATE['burak']._private_key

    emit('narrate', {'text': 'KRİTİK: Burak\'ın sunucusu hacklendi! Anahtar sızdı.'})
    emit('anim_leak', {})

    # Update History based on Key Reference (Forward Secrecy Logic)
    affected_count = 0
    for sess in STATE['history']:
        if sess['burak_priv_ref'] == leaked_key:
            sess['is_compromised'] = True
            affected_count += 1

    emit('update_history', STATE['history'])
    emit('log', {'source': 'Sistem', 'msg': f'{affected_count} geçmiş oturumun şifresi çözüldü.'})


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)