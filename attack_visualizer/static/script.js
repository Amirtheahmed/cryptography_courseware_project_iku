const socket = io();
let isInterceptMode = false;

// DOM Elements
const modal = document.getElementById('intercept-modal');
const chatInput = document.getElementById('msg-input');
const chatBtn = document.getElementById('btn-send');
const chatDisplay = document.getElementById('chat-display');
const timelineDiv = document.getElementById('timeline-bar');
const narrator = document.getElementById('narrator-text');

// --- Controls ---
function startHandshake(type) {
    socket.emit('init_handshake', {type: type});
    chatInput.disabled = true;
    chatBtn.disabled = true;
    document.getElementById('encryption-status').innerText = "Anahtar Bekleniyor...";
}

function toggleInterception() {
    isInterceptMode = document.getElementById('intercept-toggle').checked;
    socket.emit('toggle_interception', {active: isInterceptMode});
    const node = document.getElementById('node-mallory');
    if(isInterceptMode) {
        node.classList.add('active');
        document.getElementById('mallory-status').innerText = "Aktif (Durduracak)";
    } else {
        node.classList.remove('active');
        document.getElementById('mallory-status').innerText = "Pasif";
    }
}

function leakKey() {
    socket.emit('leak_key');
}

function forwardPacket() {
    // Get selected radio option
    const options = document.getElementsByName('inject');
    let selected = 'original';
    for(let op of options) if(op.checked) selected = op.value;

    modal.style.display = 'none';
    socket.emit('packet_forwarded', {inject_type: selected});
}

function sendMessage() {
    const txt = chatInput.value;
    if(!txt) return;

    // Show local message immediately
    addChatBubble(txt, 'sent');
    socket.emit('send_chat', {msg: txt});
    chatInput.value = '';
}

function addChatBubble(text, type, subtitle="") {
    const div = document.createElement('div');
    div.className = `chat-bubble chat-${type}`;
    div.innerText = text;
    if(subtitle) {
        const sub = document.createElement('div');
        sub.style.fontSize = "0.7em";
        sub.style.opacity = "0.8";
        sub.innerText = subtitle;
        div.appendChild(sub);
    }
    chatDisplay.appendChild(div);
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}

// --- Socket Events ---

socket.on('log', (data) => {
    const container = document.getElementById('log-container');
    const div = document.createElement('div');
    div.className = 'log-entry';
    // Support basic colors in message if needed, but mostly use source
    div.innerHTML = `<span class="log-source">[${data.source}]</span> ${data.msg}`;
    container.prepend(div); // Add to top
});

socket.on('narrate', (data) => {
    narrator.style.opacity = 0;
    setTimeout(() => {
        narrator.innerText = data.text;
        narrator.style.opacity = 1;
    }, 200);
});

// Animation: Packet Start
socket.on('anim_packet_start', (data) => {
    const pkt = document.getElementById('active-packet');
    pkt.style.transition = 'none';
    pkt.style.left = '10%';
    pkt.style.opacity = '1';

    // Force Reflow
    void pkt.offsetWidth;

    pkt.style.transition = 'left 1.5s linear';
    pkt.style.left = '50%'; // Move to Mallory/Middle

    setTimeout(() => {
        if(data.intercept_mode) {
            // STOP and Open Modal
            document.getElementById('modal-original-payload').innerText = data.original_payload;
            modal.style.display = 'block';
        } else {
            // Continue automatically
            socket.emit('packet_forwarded', {inject_type: 'original'});
        }
    }, 1500);
});

// Animation: Packet End
socket.on('anim_packet_end', (data) => {
    const pkt = document.getElementById('active-packet');
    pkt.style.left = '90%'; // Move to Burak
    setTimeout(() => {
        pkt.style.opacity = '0';
    }, 1000);
});

socket.on('handshake_complete', (data) => {
    chatInput.disabled = false;
    chatBtn.disabled = false;
    const badge = document.getElementById('encryption-status');
    const ardaKey = document.getElementById('key-arda');
    const burakKey = document.getElementById('key-burak');

    if(data.secure) {
        badge.innerText = "(Güvenli)";
        badge.style.color = "#22c55e";
        ardaKey.innerText = "Sır: Eşleşti ✅";
        burakKey.innerText = "Sır: Eşleşti ✅";
    } else {
        badge.innerText = "KIRILDI (Güvensiz)";
        badge.style.color = "#ef4444";
        ardaKey.innerText = "Sır: Zayıf/Uyuşmaz";
        burakKey.innerText = "Sır: Ele Geçirildi ⚠️";
    }

    document.querySelector('.chat-placeholder').style.display = 'none';
});

socket.on('chat_delivery', (data) => {
    if(data.success) {
        addChatBubble(data.decrypted, 'received');
    } else {
        addChatBubble("???????", 'received', '(Şifre Çözülemedi)');
    }
});

socket.on('update_history', (history) => {
    timelineDiv.innerHTML = '';
    if(history.length === 0) {
        timelineDiv.innerHTML = '<div class="timeline-empty">Oturum Yok</div>';
        return;
    }

    history.forEach(h => {
        const el = document.createElement('div');
        el.className = 'timeline-item';
        if(h.is_compromised) el.classList.add('compromised');

        el.innerHTML = `
            <span>${h.time}</span>
            <i class="fas ${h.is_compromised ? 'fa-lock-open' : 'fa-lock'}"></i>
        `;
        timelineDiv.appendChild(el);
    });
});

socket.on('anim_leak', () => {
    const b = document.getElementById('node-burak');
    b.style.boxShadow = "0 0 30px #ef4444";
    setTimeout(()=> b.style.boxShadow = "none", 1000);
});