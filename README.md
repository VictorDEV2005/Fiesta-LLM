# Fiesta-LLM
Repositorio para trabajo de llm

control+z |mandar a segundo plano

modo chat "ollama run tinyllama"

ps | ver los procesos

ia generativa trabaja con tokens 

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿porque el cielo es azul?",
  "stream": false
}'