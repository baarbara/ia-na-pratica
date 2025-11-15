cd node-backend
cp ../.env.example .env
# edite .env e coloque OPENAI_API_KEY
npm install
npm start
# teste com curl:
# curl -X POST -H "Content-Type: application/json" -d '{"mensagem":"Olá"}' http://localhost:3000/mensagem
