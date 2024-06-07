#importando la inagen requerida
import base64
with open("descarga.jpg","rb") as imagefile:
    convert = base64.b64encode(imagefile.read())
print(convert.decode('utf-8'))



