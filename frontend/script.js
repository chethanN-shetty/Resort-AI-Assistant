const chatBox = document.getElementById("chat-box");

function addMessage(text, className) {
  const div = document.createElement("div");
  div.className = className;
  div.innerText = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("message");
  const text = input.value;
  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  const response = await fetch("http://127.0.0.1:8000/chat/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      guest_id: 1,
      message: text
    })
  });

  const data = await response.json();
  addMessage(data.reply, "bot");
}
