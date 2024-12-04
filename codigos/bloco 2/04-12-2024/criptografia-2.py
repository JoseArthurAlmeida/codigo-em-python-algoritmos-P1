import base64

criptografado = base64.b64encode("Fuscão".encode("utf-8"))

print(criptografado)

descriptografado = base64.b64decode(criptografado)

print(str(descriptografado, "utf-8"))