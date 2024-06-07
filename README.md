# Fiesta-LLM
Repositorio para trabajo de llm

control+z |mandar a segundo plano

modo chat "ollama run tinyllama"

ps | ver los procesos

ia generativa trabaja con tokens 

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿porque el cielo es azul?",
  "stream": False
}'

git add .
git commit -m "UPDATE README"
git push -u origin main  | de la maquina a la nube que es (main)



# Llm
## paso 1 DESCARGARLO
descargar
curl -fsSL https://ollama.com/install.sh | sh

### paso 2 abrir el server
ollama serve

### Ejecutarlo en bash
ollama pull tinyllama

### Para preguntar
ollama run tinyllama ....

### Modo Chat/Detener chat

ollama run tinyllama
detener: ctrl+D

### Los token
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿Por qué el cielo es azul?",
  "stream": false
}'

### Pagina requests module
https://www.w3schools.com/python/module_requests.asp