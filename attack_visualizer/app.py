from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import sys
import os
import uuid
import hashlib
from datetime import datetime

# Path setup to include crypto_engine
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
    # Use SHA256 to turn the large integer into a 32-byte key, take first 16 chars for visual simplicity
    return hashlib.sha256(str(secret_int).encode()).hexdigest()[:16]


def xor_encrypt(msg, secret):
    """Toy encryption for visualization."""
    if secret is None: return msg
    key = derive_key(secret)
    encrypted = []
    for i, char in enumerate(msg):
        key_char = key[i % len(key)]
        encrypted.append(chr(ord(char) ^ ord(key_char)))
    return ''.join(encrypted)


def format_hex(val):
    """Format large integers as short hex strings for logging."""
    h = hex(val)[2:].upper()
    if len(h) > 16:
        return f"{h[:8]}...{h[-8:]}"
    return h


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

    # Log the Math (Act 1 Context)
    emit('log', {'source': 'Arda', 'msg': f'Private Key a generated.'})
    emit('log', {'source': 'Arda', 'msg': f'Public Key A = g^a mod p calculated.'})
    emit('log', {'source': 'Arda', 'msg': f'A = {format_hex(STATE["arda"].public_key)}'})

    emit('narrate', {'text': 'Arda Açık Anahtarını (Public Key) Burak\'a gönderiyor...'})

    # 3. Animate Packet
    emit('anim_packet_start', {
        'intercept_mode': STATE['mallory_intercept_mode'],
        'original_payload': str(STATE['arda'].public_key)[:12] + '...'
    })


@socketio.on('packet_forwarded')
def handle_forward(data):
    """Called after user manually forwards packet from modal."""
    injection_type = data.get('inject_type')

    # Default: Arda's real key goes to Burak
    payload_to_burak = STATE['arda'].public_key
    payload_to_arda = STATE['burak'].public_key  # Assuming return traffic is symmetric for normal case

    if injection_type == 'subgroup':
        # --- ACT 3: SMALL SUBGROUP ATTACK ---
        # Mallory injects P-1 (Modular -1) to BOTH parties to ensure she can decrypt
        # messages from both sides for the demo.
        payload_to_burak = DH_2048_P - 1
        payload_to_arda = DH_2048_P - 1

        STATE['shared_secrets']['mallory'] = 'DETECTED'  # Flag

        emit('log', {'source': 'Mallory', 'msg': '--------------------------------'})
        emit('log', {'source': 'Mallory', 'msg': 'ATTACK: Small Subgroup Injection'})
        emit('log', {'source': 'Mallory', 'msg': f'Injecting (P-1) to Burak.'})
        emit('log', {'source': 'Mallory', 'msg': f'Injecting (P-1) to Arda (Simulated).'})
        emit('log', {'source': 'Mallory', 'msg': 'Target Secret Space reduced to {1, P-1}'})
        emit('log', {'source': 'Mallory', 'msg': '--------------------------------'})

        emit('narrate', {'text': 'Mallory, Arda\'nın anahtarını (P-1) ile değiştirdi! Şifreleme uzayı daraltıldı.'})

    elif injection_type == 'random':
        payload_to_burak = 123456789  # Junk
        emit('log', {'source': 'Mallory', 'msg': 'DoS Attack: Sending junk data.'})
    else:
        emit('log', {'source': 'Mallory', 'msg': 'Passive Monitoring: Packet forwarded intact.'})
        emit('narrate', {'text': 'Mallory sadece izliyor. Paket değiştirilmedi.'})

    # Complete the animation to Burak
    emit('anim_packet_end', {'success': True})

    # --- Calculate Secrets ---
    try:
        # 1. Burak Computes
        # S_burak = (Received_Key)^b mod p
        burak_secret = pow(payload_to_burak, STATE['burak']._private_key, DH_2048_P)
        STATE['shared_secrets']['burak'] = burak_secret

        # Log Burak's Math
        if injection_type == 'subgroup':
            emit('log', {'source': 'Burak', 'msg': f'Computed S = (P-1)^b mod p'})
            val_display = "1 (Because b is even)" if burak_secret == 1 else "P-1 (Because b is odd)"
            emit('log', {'source': 'Burak', 'msg': f'Shared Secret: {val_display}'})
        else:
            emit('log', {'source': 'Burak', 'msg': f'Shared Secret Computed.'})

        # 2. Arda Computes
        # S_arda = (Received_Key)^a mod p
        # Note: If attack is normal, Arda uses Burak's real public key.
        # If attack is subgroup, we simulated Mallory sending P-1 back to Arda too.
        arda_secret = pow(payload_to_arda, STATE['arda']._private_key, DH_2048_P)
        STATE['shared_secrets']['arda'] = arda_secret

        # Check security status
        # Secure if secrets match AND no injection happened
        is_secure = (burak_secret == arda_secret) and (injection_type == 'original')

        # MitM Case: Both might be 1 or P-1. They might even match (if a and b have same parity).
        # But it is NOT secure because Mallory knows the key.
        if injection_type == 'subgroup':
            is_secure = False

        # Add to history
        sess_entry = {
            'id': STATE['current_session_id'],
            'time': datetime.now().strftime("%H:%M:%S"),
            'burak_priv_ref': STATE['burak']._private_key,
            'is_compromised': not is_secure  # Immediately compromised if MitM
        }

        STATE['history'].insert(0, sess_entry)
        if len(STATE['history']) > 8: STATE['history'].pop()

        emit('update_history', STATE['history'])
        emit('handshake_complete', {'secure': is_secure})

    except Exception as e:
        print(f"Handshake Error: {e}")
        emit('log', {'source': 'System', 'msg': f'Error: {str(e)}'})


@socketio.on('send_chat')
def handle_chat(data):
    """Encrypts message with calculated keys."""
    msg = data['msg']

    arda_secret = STATE['shared_secrets']['arda']
    burak_secret = STATE['shared_secrets']['burak']

    # Arda encrypts
    cipher = xor_encrypt(msg, arda_secret)

    # Send visualization
    emit('anim_chat', {'cipher': cipher[:10] + '...'})

    # Burak decrypts
    try:
        decrypted = xor_encrypt(cipher, burak_secret)
    except:
        decrypted = "????"

    # Check validity
    success = (decrypted == msg)

    emit('chat_delivery', {
        'original': msg,
        'cipher': cipher,
        'decrypted': decrypted,
        'success': success
    })

    # --- MALLORY LOGIC (Act 3 Finale) ---
    if STATE['shared_secrets']['mallory'] == 'DETECTED':
        # Mallory Brute Forces the small subgroup {1, P-1}
        emit('log', {'source': 'Mallory', 'msg': 'Intercepted Ciphertext.'})
        emit('log', {'source': 'Mallory', 'msg': 'Brute-forcing Subgroup {1, P-1} ...'})

        # Try Key = 1
        guess_1 = xor_encrypt(cipher, 1)
        # Try Key = P-1
        guess_2 = xor_encrypt(cipher, DH_2048_P - 1)

        cracked_msg = None
        key_used = None

        # Simple heuristic: is it ASCII printable? (In real life, we look for headers)
        if guess_1 == msg:
            cracked_msg = guess_1
            key_used = "1"
        elif guess_2 == msg:
            cracked_msg = guess_2
            key_used = "P-1"

        if cracked_msg:
            emit('log', {'source': 'Mallory', 'msg': f'SUCCESS! Found Key: {key_used}'})
            emit('log', {'source': 'Mallory', 'msg': f'DECRYPTED: "{cracked_msg}"'})
        else:
            emit('log', {'source': 'Mallory', 'msg': 'Failed to crack (Parity Mismatch?)'})


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

    emit('log', {'source': 'System', 'msg': '--------------------------------'})
    emit('log', {'source': 'System', 'msg': 'SECURITY ALERT: Static Key Leaked'})
    emit('log', {'source': 'System', 'msg': f'Leaked Private Key: {str(leaked_key)[:8]}...'})

    # Update History based on Key Reference (Forward Secrecy Logic)
    affected_count = 0
    for sess in STATE['history']:
        if sess['burak_priv_ref'] == leaked_key:
            if not sess['is_compromised']:  # Don't double count already broken ones
                sess['is_compromised'] = True
                affected_count += 1

    emit('update_history', STATE['history'])

    if affected_count > 0:
        emit('log', {'source': 'System', 'msg': f'FAIL: {affected_count} past sessions decrypted!'})
    else:
        emit('log', {'source': 'System', 'msg': 'SUCCESS: Past sessions safe (Forward Secrecy).'})

    emit('log', {'source': 'System', 'msg': '--------------------------------'})


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)