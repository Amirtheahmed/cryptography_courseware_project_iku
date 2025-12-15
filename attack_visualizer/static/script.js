const socket = io();

// UI Elements
const packet = document.getElementById('active-packet');
const logContainer = document.getElementById('log-container');
const malloryNode = document.getElementById('node-mallory');
const narratorText = document.getElementById('narrator-text');
const historyList = document.getElementById('history-list');

// --- Control Functions ---
function startHandshake(type) {
    socket.emit('init_handshake', {type: type});
}

function toggleAttack() {
    socket.emit('toggle_attack');
}

function leakKey() {
    socket.emit('leak_key');
}

// --- WebSocket Handlers ---

socket.on('narrate', (data) => {
    narratorText.style.opacity = '0';
    setTimeout(() => {
        narratorText.innerText = data.text;
        narratorText.style.opacity = '1';
    }, 200);
});

socket.on('log', (data) => {
    const entry = document.createElement('div');
    entry.className = `log-entry log-${data.type}`;
    const time = new Date().toLocaleTimeString('tr-TR');
    entry.innerHTML = `<span class="log-time">[${time}]</span> <span class="log-source">${data.source}:</span> ${data.msg}`;
    logContainer.prepend(entry);
});

socket.on('update_history', (data) => {
    historyList.innerHTML = '';
    if(data.history.length === 0) {
        historyList.innerHTML = '<tr><td colspan="4" style="text-align:center;">Henüz oturum yok</td></tr>';
        return;
    }

    data.history.forEach(sess => {
        const row = document.createElement('tr');
        // Add class if compromised
        if(sess.status === 'ÇÖZÜLDÜ') {
            row.classList.add('row-compromised');
        } else {
            row.classList.add('row-secure');
        }

        row.innerHTML = `
            <td>${sess.time}</td>
            <td>${sess.mode}</td>
            <td style="font-family:monospace">${sess.secret_hint}</td>
            <td>${sess.status === 'ÇÖZÜLDÜ' ? '<i class="fas fa-unlock text-danger"></i>' : '<i class="fas fa-lock text-success"></i>'}</td>
        `;
        historyList.appendChild(row);
    });
});

socket.on('update_mallory', (data) => {
    const btn = document.getElementById('btn-mitm');
    if(data.active) {
        malloryNode.classList.add('active');
        document.getElementById('status-mallory').innerText = "Mod: ARAYA GİRİYOR";
        btn.classList.add('active-state');
    } else {
        malloryNode.classList.remove('active');
        document.getElementById('status-mallory').innerText = "Mod: Pasif";
        btn.classList.remove('active-state');
    }
});

socket.on('anim_packet', (data) => {
    // Show packet
    packet.style.opacity = '1';
    packet.innerHTML = `<i class="fas fa-key"></i>`;
    packet.style.backgroundColor = '#ffffff';
    packet.style.color = '#000';
    packet.style.left = '10%'; // Start at arda
    packet.style.transition = 'none';

    // Trigger Reflow
    void packet.offsetWidth;

    // Animate
    packet.style.transition = 'left 2s ease-in-out';

    if (data.intercepted) {
        // Stop at Mallory
        packet.style.left = '50%';
        setTimeout(() => {
            packet.innerHTML = `<i class="fas fa-skull"></i>`; // Change to malicious
            packet.style.backgroundColor = '#da3633';
            packet.style.color = '#fff';

            // Resume to burak after brief pause
            setTimeout(() => {
                packet.style.left = '90%';
                setTimeout(() => {
                    packet.style.opacity = '0';
                    socket.emit('complete_handshake'); // Tell server animation is done
                }, 2000);
            }, 1000);
        }, 2000);
    } else {
        // Go straight to burak
        packet.style.left = '90%';
        setTimeout(() => {
            packet.style.opacity = '0';
            socket.emit('complete_handshake');
        }, 2000);
    }
});

socket.on('update_status', (data) => {
    const el = document.getElementById(`status-${data.actor}`);
    const keyEl = document.getElementById(`key-${data.actor}`);

    el.innerText = data.status;
    keyEl.innerText = `Sır: ${data.secret}`;

    if (data.status === 'ELE GEÇİRİLDİ' || data.status === 'KIRILDI') el.style.color = '#da3633';
    if (data.status === 'GÜVENLİ') el.style.color = '#2ea043';
});

socket.on('anim_key_gen', (data) => {
    const node = document.getElementById(`node-${data.target}`);
    const originalColor = node.style.borderColor;
    node.style.borderColor = "#58a6ff";
    node.style.boxShadow = "0 0 15px #58a6ff";
    setTimeout(() => {
        node.style.borderColor = "";
        node.style.boxShadow = "";
    }, 500);
});

socket.on('anim_leak', (data) => {
    const burak = document.getElementById('node-burak');
    burak.classList.add('shaking');
    burak.style.borderColor = "#da3633";
    burak.style.boxShadow = "0 0 30px #da3633";
    setTimeout(() => {
        burak.classList.remove('shaking');
        burak.style.borderColor = "";
        burak.style.boxShadow = "none";
    }, 1000);
});