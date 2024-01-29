entrada = input()
entrada_nova = []
entrada_alreves = []
devnull = []

for caracter in reversed(entrada):
    if caracter == " ":
        devnull.append(caracter)
    else:
        entrada_alreves.append(caracter.upper())

for caracter in entrada:
    if caracter == " ":
        devnull.append(caracter)
    else:
        entrada_nova.append(caracter.upper())

if entrada_nova == entrada_alreves:
    print("Es palindrum")
else:
    print("No es")
