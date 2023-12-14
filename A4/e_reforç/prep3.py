numeros = [8, 7, 6, 5, 4, 3, 2, 1]
lletres = (" a  b  c  d  e  f  h ")

for i in range(8):
    print(f"\n{numeros[i]}", end="")
    for j in range(8):
        if (j + i) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    if i == 7:
        print()
        print(lletres)

posicion_numerica = int(input("introduce la posicion numerica para ver los movimientos de la torre (1-8): "))
posicion_alfanumerica = str(input("introduce la posicion numerica para ver los movimientos de la torre (a-h): "))

for i in range(8):
    print(f"\n{numeros[i]}", end="")
    for j in range(8):
        if (j + i) % 2 == 0:
            if posicion_numerica == j:
                print(f"{'*' * 8}", end="")
            print("⬜", end="")
        else:
            if posicion_numerica == j:
                print(f"{'*' * 8}", end="")
            print("⬛", end="")
    if i == 7:
        print()
        print(lletres)