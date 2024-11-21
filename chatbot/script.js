const chatBody = document.getElementById("chat-body");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

// Fungsi untuk menambahkan pesan ke chat
function addMessage(message, isBot = false) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("chat-message", isBot ? "bot-message" : "user-message");
    messageElement.textContent = message;
    chatBody.appendChild(messageElement);
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Fungsi untuk mengirim pesan ke backend
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, false); // Tampilkan pesan pengguna
    userInput.value = "";

    try {
        const response = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });

        const data = await response.json();
        addMessage(data.reply, true); // Tampilkan respons bot
    } catch (error) {
        console.error("Error:", error);
        addMessage("Terjadi kesalahan. Coba lagi nanti.", true);
    }
}

// Event handler tombol kirim
sendButton.addEventListener("click", sendMessage);

// Event handler untuk tombol Enter
userInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") sendMessage();
});
