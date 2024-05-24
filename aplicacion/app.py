import requests

url = 'http://127.0.0.1:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt":"¿porque el cielo es azul?",
  "stream": False
}

x = requests.post(url, json = myobj)

print(x.text)