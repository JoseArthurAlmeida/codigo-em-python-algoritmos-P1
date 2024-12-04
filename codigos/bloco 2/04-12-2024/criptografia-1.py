import base64

entrada = input("Digite um texto para criptografar: ")
textoBinario = entrada.encode("utf-8")

textoCodificado = base64.b64encode(textoBinario)
print(f"String criptografada: {textoCodificado}")  

textoDecodificado = base64.b64decode(textoCodificado)
print(f"Texto descriptografado: {textoDecodificado.decode("utf-8")}")