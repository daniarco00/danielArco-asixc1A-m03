cadena, posicio = input(), int(input())
cont = 0

for car in cadena:
    if cont == posicio:
        print(car)
    cont += 1
