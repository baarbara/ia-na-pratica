<p align="center">
  <img src="https://raw.githubusercontent.com/baarbara/ia-na-pratica/main/assets/capa-release.png" alt="Capa — IA na Prática" width="900" />
</p>
# IA na Prática — Templates de Código  
### IA in Practice — Code Templates

[![License](https://img.shields.io/github/license/baarbara/ia-na-pratica)](LICENSE)
![Repo Size](https://img.shields.io/github/repo-size/baarbara/ia-na-pratica)
![Stars](https://img.shields.io/github/stars/baarbara/ia-na-pratica?style=social)

> **PT-BR:** Repositório oficial de apoio ao livro *"IA na Prática — Da Teoria ao Site Inteligente"* (2025).  
> **EN:** Official support repository for the book *"AI in Practice — From Theory to Intelligent Websites"* (2025).

Este repositório reúne exemplos completos, organizados e prontos para uso.  
This repository provides complete, organized, ready-to-use examples.

Inclui / Includes:
- Chatbot em Python com Gradio / Python chatbot with Gradio  
- Backend Node.js com OpenAI / Node.js backend using OpenAI  
- Sistema de recomendação / Recommendation system  
- Aplicativo em Streamlit / Streamlit application  
- Arquivos `.env` e boas práticas / `.env` templates & best practices  

---

## Tecnologias usadas | Technologies Used

- **Python 3.10+**
- **Node.js 18+**
- **OpenAI API (Responses API)**
- **Gradio**
- **Streamlit**
- **Express.js**
- **scikit-learn**
- **Pandas**

---

## Estrutura do Repositório | Repository Structure

```bash

ia-na-pratica/
├── python-chatbot/
│ ├── app_gradio.py
│ ├── requirements.txt
│
├── node-backend/
│ ├── server.js
│ ├── package.json
│ ├── .gitignore
│
├── recommender/
│ ├── recommender.py
│ ├── dataset_example.csv
│ ├── requirements.txt
│
├── streamlit-app/
│ ├── app_streamlit.py
│ ├── requirements.txt
│
├── .env.example
├── README.md
├── LICENSE
└── .gitignore

```

---

## Configuração da API | API Key Setup

PT-BR / EN

Antes de rodar qualquer exemplo: / Before running any example:

cp .env.example .env


Depois, defina sua chave: / Set your Key:

OPENAI_API_KEY=sua_chave_aqui


**Nunca exponha sua chave em repositórios públicos.**  
**Never expose your API key in public repositories.**

---

# Exemplos incluídos | Included Examples

---

## 1. Chatbot em Python (Gradio) | Python Chatbot (Gradio)

**PT-BR:** Um chatbot funcional usando o modelo **gpt-5.1-mini**.  
**EN:** A functional chatbot powered by **gpt-5.1-mini**.

### Executar | Run:

- cd python-chatbot
- pip install -r requirements.txt
- python app_gradio.py


---

## 2. Backend Node.js (Express) | Node.js Backend (Express)

Endpoint:

POST /mensagem


### Executar | Run:

- cd node-backend
- npm install
- npm start


---

## 3. Sistema de Recomendação | Recommendation System

Inclui / Includes:
- Normalização de dados / Data normalization  
- Similaridade por cosseno / Cosine similarity  
- Recomendações básicas / Basic recommendations  

### Executar | Run:

- cd recommender
- pip install -r requirements.txt
- python recommender.py


---

## 4. App Streamlit | Streamlit App

Prototipação rápida com interface amigável.  
Fast prototyping with a modern UI.

### Executar | Run:

- cd streamlit-app
- pip install -r requirements.txt
- streamlit run app_streamlit.py


---

# Boas práticas incluídas | Included Best Practices

- Uso de .env para segurança / Environment variable isolation
- Tratamento de erros / Error handling
- x-api-key no backend / Optional API key header
- .gitignore adequado / Proper .gitignore
- Rate-limiting & Helmet (versão avançada) / Advanced security options  

---

# Requisitos gerais | General Requirements

- Python 3.10+  
- Node.js 18+  
- Chave ativa da OpenAI / Active OpenAI API key  
- Conexão com internet / Internet connection  

---

# Sobre o livro | About the Book

Este repositório acompanha capítulos como:  
This repository supports chapters such as:

| Capítulo (PT) | Chapter (EN) | Tema | Directory |
|---------------|--------------|------|-----------|
| Cap. 3 | Ch. 3 | Chatbots | python-chatbot |
| Cap. 5 | Ch. 5 | Backend inteligente | node-backend |
| Cap. 6 | Ch. 6 | Recomendação | recommender |
| Cap. 7 | Ch. 7 | Prototipagem | streamlit-app |

---

# Contribuições | Contributions

**PT-BR:** Pull Requests são bem-vindas!  
**EN:** Pull Requests are welcome!  

Mantenha o código claro, didático e seguro.  
Keep code clean, educational, and secure.

---

# Licença | License

MIT License — veja `LICENSE`.  
MIT License — see `LICENSE`.

---

# Contato | Contact
Autora / Author: Barbara P. Tavora 

📧 **baarbara+livroia@gmail.com**  
🔗 **https://www.linkedin.com/in/barbaratavora**

**PT-BR:** Obrigada por utilizar este material!  
**EN:** Thank you for using this material!
