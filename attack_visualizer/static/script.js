const socket = io();

// UI Elements
const packet = document.getElementById('active-packet');
const logContainer = document.getElementById('log-container');
const malloryNode = document.getElementById('node-mallory');

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

socket.on('log', (data) => {
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    const time = new Date().toLocaleTimeString();
    entry.innerHTML = `<span class="log-time">[${time}]</span> <span class="log-source">${data.source}:</span> ${data.msg}`;
    logContainer.prepend(entry);
});

socket.on('update_mallory', (data) => {
    if(data.active) {
        malloryNode.classList.add('active');
        document.getElementById('status-mallory').innerText = "Mode: INTERCEPTING";
    } else {
        malloryNode.classList.remove('active');
        document.getElementById('status-mallory').innerText = "Mode: Passive";
    }
});

socket.on('anim_packet', (data) => {
    // Show packet
    packet.style.opacity = '1';
    packet.innerHTML = `<i class="fas fa-key"></i>`;
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

    el.innerText = data.status.toUpperCase();
    keyEl.innerText = `Secret: ${data.secret}`;

    if (data.status === 'compromised') el.style.color = '#da3633';
    if (data.status === 'secure') el.style.color = '#2ea043';
});

socket.on('anim_leak', (data) => {
    const burak = document.getElementById('node-burak');
    burak.style.boxShadow = "0 0 30px #da3633";
    setTimeout(() => { burak.style.boxShadow = "none"; }, 500);
});