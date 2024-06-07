import requests
import json as js

#importando la inagen requerida
import base64
with open("descarga.jpg","rb") as imagefile:
    convert = base64.b64encode(imagefile.read())
print(convert.decode('utf-8'))


uri="http://localhost:11434/api/generate -d" 
data= {"model": "llava","prompt":"What is in this picture?","images": []}

response=requests.post(uri, js=data)
response=json.loads(response, text)

print(response['response'])