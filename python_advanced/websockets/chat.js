const socket = new WebSocket('ws://localhost:8000/ws');
const messages = document.getElementById('messages');
const form = document.getElementById('form');
const input = document.getElementById('input');

function addMessage (text, className) {
  const li = document.createElement('li');
  li.textContent = text;
  li.className = className;
  messages.appendChild(li);
  messages.scrollTop = messages.scrollHeight;
}

socket.onmessage = (event) => addMessage(event.data, 'received');

form.onsubmit = (event) => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text || socket.readyState !== WebSocket.OPEN) return;
  socket.send(text);
  addMessage(text, 'sent');
  input.value = '';
};
