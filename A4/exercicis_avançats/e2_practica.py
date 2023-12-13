x = 11
while x > 10:
    num1 = [int(x) for x in input().split()]
    if len(num1) != 10:
        num1 = [int(x) for x in input().split()]
    else:
        x = 9

positivo = []
negativo = []
zero = []

for x in num1:
    if x > 0:
        positivo.append(x)
    elif x < 0:
        negativo.append(x)
    elif x == 0:
        zero.append(x)

print(f"Numeros positius: {positivo}.\n"
      f"Numeros negatius: {negativo}. \n"
      f"Numeros igual a 0 {len(zero)} repeticions")




