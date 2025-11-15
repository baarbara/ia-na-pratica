import express from "express";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(express.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.post("/mensagem", async (req, res) => {
  try {
    const pergunta = req.body.mensagem;
    if (!pergunta) return res.status(400).send("Campo 'mensagem' é obrigatório.");

    const resposta = await client.responses.create({
      model: "gpt-5.1-mini",
      input: pergunta
    });

    // Pegue o texto retornado de acordo com o SDK
    const texto = resposta.output_text ?? JSON.stringify(resposta);
    res.send({ resposta: texto });
  } catch (err) {
    console.error("Erro ao chamar a API:", err);
    res.status(500).send({ error: "Erro interno ao gerar resposta." });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
