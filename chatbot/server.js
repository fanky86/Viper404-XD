const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const { Configuration, OpenAIApi } = require("openai");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Masukkan API Key OpenAI
const configuration = new Configuration({
    apiKey: "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", // Ganti dengan API Key Anda
});
const openai = new OpenAIApi(configuration);

// Endpoint untuk mengirim pesan ke OpenAI API
app.post("/chat", async (req, res) => {
    const { message } = req.body;

    try {
        const response = await openai.createChatCompletion({
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: message }],
        });

        const botMessage = response.data.choices[0].message.content;
        res.json({ reply: botMessage });
    } catch (error) {
        console.error("Error:", error);
        res.status(500).json({ error: "Terjadi kesalahan pada server" });
    }
});

// Jalankan server
const PORT = 5000;
app.listen(PORT, () => console.log(`Server berjalan di http://localhost:${PORT}`));
