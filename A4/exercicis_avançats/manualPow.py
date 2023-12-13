

base = int(input("Introdueix la base de la potencia: "))
exponent = int(input("Introdueix l'exponent de la potencia: "))

potencia = 1
for x in range(exponent):
    potencia *= base

print(potencia)