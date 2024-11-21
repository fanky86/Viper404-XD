const chatBody = document.getElementById("chat-body");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

// Fungsi untuk menampilkan pesan di chat
function addMessage(message, isBot = false) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("chat-message", isBot ? "bot-message" : "user-message");
    messageElement.textContent = message;
    chatBody.appendChild(messageElement);
    chatBody.scrollTop = chatBody.scrollHeight; // Auto-scroll ke bawah
}

// Fungsi untuk merespons pesan user
function getBotResponse(userMessage) {
    // Respons sederhana
    const responses = {
        "halo": "Halo juga! Ada yang bisa saya bantu?",
        "siapa kamu?": "Saya adalah chatbot sederhana!",
        "apa kabar?": "Saya selalu baik, bagaimana dengan Anda?",
        "selamat tinggal": "Sampai jumpa lagi!"
    };

    // Jika tidak ditemukan respons, gunakan default
    return responses[userMessage.toLowerCase()] || "Maaf, saya tidak mengerti.";
}

// Event ketika tombol "Kirim" ditekan
sendButton.addEventListener("click", () => {
    const userMessage = userInput.value.trim();
    if (userMessage) {
        addMessage(userMessage, false); // Tambahkan pesan user
        const botResponse = getBotResponse(userMessage); // Dapatkan respons bot
        setTimeout(() => addMessage(botResponse, true), 500); // Tambahkan pesan bot dengan delay
        userInput.value = ""; // Hapus input setelah terkirim
    }
});

// Event ketika tombol Enter ditekan
userInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        sendButton.click();
    }
});
