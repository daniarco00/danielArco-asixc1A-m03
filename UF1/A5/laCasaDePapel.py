
lista = [0]*11 #, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

entrada = input().split()
clave = 0
posicion = 0

while clave != -1:
    for i in range(0, len(entrada)):
        if entrada[posicion] in entrada:
            lista[entrada[posicion]] + 1
            posicion += 1


print(lista)
