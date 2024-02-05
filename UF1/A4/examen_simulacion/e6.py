"""
Danil Arco Guasch
15/12/2023
ASIXc A M03 UF1
Descripció: MatrixDiagonals

"""
try:
    lista = [0, 1, 2, 3, 4, 5, 6, 7]
    lista_inversa = [7, 6, 5, 4, 3, 2, 1, 0]

    for i in range(8):
        print(f"\n ", end="")
        for j in range(8):
            if (i + j) % 2 == 0:
                if i == lista[i] and j == lista[i]:
                    print(" 1 ", end="")
                else:
                    print(f" 0 ", end="")
            else:
                if j == lista_inversa[i] and j == lista_inversa[i]:
                    print(" 2 ", end="")
                else:
                    print(f" 0 ", end="")
        if i == 7:
            print()
except:
    print("Error")