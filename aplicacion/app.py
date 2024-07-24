import requests

api_key = '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'
url = "https://api.groq.com/openai/v1/chat/completions"  # Verifica la URL según la documentación

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {
            "role": "system",
            "content": "Eres una inteligencia artificial diseñada para crear cuentos, fábulas y libros educativos para niños de 6 a 8 años. Ayuda a los profesores a generar historias sobre diversos temas de grados."
        },
        {
            "role": "user",
            "content": input("PROMPT: ")
        }
    ],
    "model": "llama3-70b-8192",  # Usa guiones en lugar de puntos
    "temperature": 1,
    "max_tokens": 1024,
    "top_p": 1
}

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Levanta una excepción si hay un error HTTP
    response_data = response.json()

    if 'choices' in response_data and response_data['choices']:
        print(response_data['choices'][0]['message']['content'])
    else:
        print("No se encontraron resultados en la respuesta de la API.")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
except json.JSONDecodeError:
    print("Error al decodificar la respuesta JSON.")
except KeyError as e:
    print(f"Clave faltante en la respuesta JSON: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
