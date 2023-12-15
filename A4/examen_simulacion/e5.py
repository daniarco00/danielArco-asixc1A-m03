try:
    n = input("Pon las coordenadas:  ").split()
    cordx = int(n[0])
    cordy = int(n[1])
    pieza = int(input(" 1) Torre \n 2) Alfil \n 3) Reina \n Escriba en numeros \n"))
    for y in range(1, 9):
        if y // 2 != y / 2:
            aux1 = "B"
            aux2 = "N"
        else:
            aux1 = "N"
            aux2 = "B"
        if pieza == 1:
            for j in range(1, 9):
                if (cordx == j or cordy == y) and j == 8:
                    print("*", end="\n")
                elif cordx == j or cordy == y:
                    print("*", end=" ")
                elif j == 8:
                    print(aux2, end="\n")
                elif j // 2 != j / 2:
                    print(aux1, end=" ")
                else:
                    print(aux2, end=" ")
        elif pieza == 2:
            for x in range(1, 9):
                if (cordx + cordy == y + x or cordx - cordy == x - y) and x == 8:
                    print("*", end="\n")
                elif cordx + cordy == y + x or cordx - cordy == x - y:
                    print("*", end=" ")
                elif x == 8:
                    print(aux2, end="\n")
                elif x // 2 != x / 2:
                    print(aux1, end=" ")
                else:
                    print(aux2, end=" ")
        elif pieza == 3:
            for l in range(1, 9):
                if ((cordx == l or cordy == y) or (cordx + cordy == y + l or cordx - cordy == l - y)) and l == 8:
                    print("*", end="\n")
                elif (cordx == l or cordy == y) or (cordx + cordy == y + l or cordx - cordy == l - y):
                    print("*", end=" ")
                elif l == 8:
                    print(aux2, end="\n")
                elif l // 2 != l / 2:
                    print(aux1, end=" ")
                else:
                    print(aux2, end=" ")
        else:
            print("Introduzca una pieza valida")
except:
    print("Value Error")