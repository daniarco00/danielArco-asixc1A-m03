

lista = [int(x) for x in input().split()]

lista_positivos = []
for i in lista:
    if i > 0:
        lista_positivos.append(i)
    else:
        continue

print(sum(lista_positivos))
