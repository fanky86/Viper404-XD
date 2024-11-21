const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const { OpenAI } = require("openai");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Ganti "YOUR_OPENAI_API_KEY" dengan API key Anda
const openai = new OpenAI({
    apiKey: "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",
});

// Endpoint untuk menerima permintaan chat
app.post("/chat", async (req, res) => {
    const { message } = req.body;

    try {
        const response = await openai.chat.completions.create({
            model: "gpt-3.5-turbo", // Model yang digunakan
            messages: [{ role: "user", content: message }], // Pesan pengguna
        });

        const botMessage = response.choices[0].message.content;
        res.json({ reply: botMessage });
    } catch (error) {
        console.error("Error:", error);
        res.status(500).json({ error: "Terjadi kesalahan pada server." });
    }
});

// Jalankan server
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server berjalan di http://localhost:${PORT}`);
});
