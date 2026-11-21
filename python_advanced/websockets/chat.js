const WS_URL = "ws://localhost:8000/ws";

const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const formEl = document.getElementById("chat-form");
const inputEl = document.getElementById("message-input");
const sendButtonEl = document.getElementById("send-button");

const socket = new WebSocket(WS_URL);

function appendMessage(text, type) {
    const msgEl = document.createElement("div");
    msgEl.className = `message ${type}`;
    msgEl.textContent = text;
    messagesEl.appendChild(msgEl);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function setConnected(isConnected) {
    statusEl.textContent = isConnected ? "Connected" : "Disconnected";
    statusEl.className = `status ${isConnected ? "connected" : "disconnected"}`;
    sendButtonEl.disabled = !isConnected;
}

socket.onopen = () => {
    setConnected(true);
    appendMessage("Connected to WebSocket server.", "system");
};

socket.onmessage = (event) => {
    appendMessage(`Server: ${event.data}`, "received");
};

socket.onclose = () => {
    setConnected(false);
    appendMessage("Connection closed.", "system");
};

socket.onerror = () => {
    appendMessage("WebSocket error occurred.", "system");
};

formEl.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = inputEl.value;
    if (!text || socket.readyState !== WebSocket.OPEN) {
        return;
    }
    socket.send(text);
    appendMessage(`You: ${text}`, "sent");
    inputEl.value = "";
    inputEl.focus();
});
