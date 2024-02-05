


n = int(input())

lista = []

for x in range(1,n):
    if n % x == 0:
        lista.append(x)

print(lista)