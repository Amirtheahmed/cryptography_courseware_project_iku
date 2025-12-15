from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
import os
import uuid
from datetime import datetime

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
    "mode": "ephemeral",  # 'ephemeral' or 'static'
    "history": []  # Stores past sessions: {id, time, mode, burak_key, status}
}


# --- Helper Functions ---

def narrate(text):
    """Sends a subtitle explanation to the frontend."""
    emit('narrate', {'text': text})


def log_event(source, message, type="info"):
    """Sends a log entry."""
    emit('log', {'source': source, 'msg': message, 'type': type})


def update_history_ui():
    """Sends the session history list to frontend."""
    # Convert private keys to string for display/comparison logic, hide actual values
    safe_history = []
    for sess in STATE['history']:
        safe_history.append({
            'id': sess['id'],
            'time': sess['time'],
            'mode': sess['mode'],
            'status': sess['status'],  # 'secure', 'compromised'
            'secret_hint': sess['secret_hint']
        })
    emit('update_history', {'history': safe_history})


# --- Routes & Sockets ---

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('init_handshake')
def handle_handshake(data):
    STATE['mode'] = data.get('type')

    narrate("1. Adım: Taraflar anahtar çiftlerini hazırlıyor. Arda her zaman yeni (Ephemeral) anahtar üretir.")

    # 1. Arda Generates Key (Always Ephemeral)
    STATE['arda'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    log_event("Arda", f"Özel Anahtar Üretildi: {str(STATE['arda']._private_key)[:6]}...", "info")
    emit('anim_key_gen', {'target': 'arda'})

    # 2. Burak Generates Key
    if STATE['mode'] == 'static' and STATE['burak']:
        narrate("Burak 'Statik' modda. Daha önceki uzun vadeli anahtarını kullanıyor.")
        log_event("Burak", "Mevcut STATİK Özel Anahtar yüklendi (Değişmedi).", "warning")
    else:
        narrate("Burak 'Geçici' (Ephemeral) modda. Bu oturum için yeni bir anahtar üretiyor.")
        STATE['burak'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
        log_event("Burak", f"Yeni Geçici (Ephemeral) Anahtar Üretildi: {str(STATE['burak']._private_key)[:6]}...",
                  "info")
        emit('anim_key_gen', {'target': 'burak'})

    # 3. Public Key Exchange Animation
    narrate("2. Adım: Açık anahtarlar (Public Keys) güvensiz kanal üzerinden gönderiliyor.")
    emit('anim_packet', {
        'from': 'arda', 'to': 'burak',
        'payload': f'AçıkA: {str(STATE["arda"].public_key)[:8]}...',
        'intercepted': STATE['mallory_active']
    })


@socketio.on('complete_handshake')
def finalize_handshake():
    """Calculates shared secrets after animation finishes"""

    session_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime("%H:%M:%S")

    if STATE['mallory_active']:
        narrate("SALDIRI TESPİT EDİLDİ: Mallory araya girdi ve Arda'nın anahtarını 'p-1' ile değiştirdi!")

        # ATTACK: Subgroup Confinement
        p_minus_1 = DH_2048_P - 1

        # Burak computes secret using P-1
        burak_secret = pow(p_minus_1, STATE['burak']._private_key, DH_2048_P)

        log_event("Mallory", "ENJEKSİYON: Arda'nın anahtarı yerine (P-1) gönderildi!", "danger")
        log_event("Burak", "Ortak Sır Hesaplandı (Manipüle Edilmiş)", "danger")

        emit('update_status', {'actor': 'burak', 'status': 'ELE GEÇİRİLDİ', 'secret': str(burak_secret)})
        emit('update_status', {'actor': 'mallory', 'status': 'KIRILDI', 'secret': '1 veya P-1'})

        narrate("Sonuç: Burak'ın hesapladığı sır sadece 1 veya -1 olabilir. Mallory şifreyi 2 denemede çözer.")

    else:
        # Normal DH
        arda_s = STATE['arda'].generate_shared_secret(STATE['burak'].public_key)
        burak_s = STATE['burak'].generate_shared_secret(STATE['arda'].public_key)

        narrate("3. Adım: Başarılı! İki taraf da matematiksel olarak aynı Ortak Sırrı (Shared Secret) türetti.")
        log_event("Sistem", "Kanal Güvenli. Ortak Sır oluşturuldu.", "success")

        emit('update_status', {'actor': 'arda', 'status': 'GÜVENLİ', 'secret': str(arda_s)[:10]})
        emit('update_status', {'actor': 'burak', 'status': 'GÜVENLİ', 'secret': str(burak_s)[:10]})

        # Add to History (For Forward Secrecy Demo)
        new_session = {
            'id': session_id,
            'time': timestamp,
            'mode': 'Statik' if STATE['mode'] == 'static' else 'Geçici',
            'burak_key_ref': STATE['burak']._private_key,  # Store actual ref to check equality later
            'status': 'GÜVENLİ',
            'secret_hint': str(burak_s)[:8]
        }
        STATE['history'].insert(0, new_session)  # Prepend
        # Keep only last 5
        if len(STATE['history']) > 5:
            STATE['history'].pop()

        update_history_ui()
        narrate("Oturum kaydedildi. 'İleriye Dönük Gizlilik' testi için yeni oturumlar açabilirsiniz.")


@socketio.on('toggle_attack')
def toggle_attack():
    STATE['mallory_active'] = not STATE['mallory_active']
    status = "AKTİF" if STATE['mallory_active'] else "PASİF"

    if STATE['mallory_active']:
        narrate("Mallory dinleme moduna geçti. 'Small Subgroup' saldırısı için hazır.")
    else:
        narrate("Mallory devredışı bırakıldı.")

    log_event("Mallory", f"Araya Girme Modu: {status}", "warning")
    emit('update_mallory', {'active': STATE['mallory_active']})


@socketio.on('leak_key')
def leak_key():
    """Forward Secrecy Demo: Leak Burak's CURRENT Key and check history"""
    if not STATE['burak']:
        narrate("Hata: Sızdırılacak bir anahtar yok. Önce oturum başlatın.")
        return

    current_key = STATE['burak']._private_key
    key_str = str(current_key)

    narrate("KRİTİK: Burak'ın sunucusu hacklendi! Saldırgan şu anki özel anahtarı ele geçirdi.")
    log_event("Sistem", f"KRİTİK: Burak'ın Anahtarı Sızdı: {key_str[:8]}...", "danger")
    emit('anim_leak', {'key': key_str})

    # Check History for Forward Secrecy Failure
    narrate("Analiz: Saldırgan sızan anahtarı kullanarak GEÇMİŞ oturumları çözmeye çalışıyor...")

    compromised_count = 0
    for sess in STATE['history']:
        # If the session used the SAME key as the leaked one, it is compromised.
        if sess['burak_key_ref'] == current_key:
            sess['status'] = 'ÇÖZÜLDÜ'
            compromised_count += 1
        else:
            # If Ephemeral was used, keys are different, so it stays Secure
            pass

    update_history_ui()

    if compromised_count > 1:
        narrate(
            f"SONUÇ: İleriye Dönük Gizlilik YOK! Statik anahtar yüzünden {compromised_count} geçmiş oturum çözüldü.")
    elif compromised_count == 1:
        narrate("SONUÇ: Sadece güncel oturum etkilendi. Geçmiş oturumlar (farklı anahtarlı) güvende.")
    else:
        narrate("SONUÇ: Geçmiş kayıtlar güvende.")


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)