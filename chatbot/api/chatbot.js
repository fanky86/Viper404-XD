const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY, // API Key OpenAI dari environment variable
});

const openai = new OpenAIApi(configuration);

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Only POST method is allowed" });
    return;
  }

  const { message } = req.body;

  if (!message) {
    res.status(400).json({ error: "Message is required" });
    return;
  }

  try {
    const completion = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: message }],
    });

    const responseMessage = completion.data.choices[0].message.content;

    res.status(200).json({ response: responseMessage });
  } catch (error) {
    console.error("Error calling OpenAI API:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
};
