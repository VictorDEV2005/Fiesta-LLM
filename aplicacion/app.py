import requests
import json

url = "https://api.groq.com/openai/v1/chat/completions"

API_KEY = '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'

headers = {
    "content-type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "messages": [
        {
            "role": "system",
            "content": "Un profesor de inglés es un educador dedicado a enseñar el idioma inglés a estudiantes de diferentes niveles y edades."
        },
        {
            "role": "user",
            "content": "¿Que son los adjetivo?"
        }
    ],
    "model": "llama3-8b-8192",
    "temperature": 1,
    "max_tokens": 1024,
    "top_p": 1,
    "stream": False,
    "stop": None
}

response = requests.post(url, json=data, headers=headers)
response_data = json.loads(response.text)

print(response_data['choices'][0]['message']['content'])
