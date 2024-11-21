const { OpenAI } = require("openai");

const openai = new OpenAI({
    apiKey: "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", // Ganti dengan API Key Anda
});

export default async function handler(req, res) {
    if (req.method === "POST") {
        const { message } = req.body;

        try {
            const response = await openai.chat.completions.create({
                model: "gpt-3.5-turbo",
                messages: [{ role: "user", content: message }],
            });

            const botMessage = response.choices[0].message.content;
            res.status(200).json({ reply: botMessage });
        } catch (error) {
            console.error("Error:", error);
            res.status(500).json({ error: "Terjadi kesalahan pada server." });
        }
    } else {
        res.status(405).json({ error: "Metode tidak diizinkan." });
    }
}
