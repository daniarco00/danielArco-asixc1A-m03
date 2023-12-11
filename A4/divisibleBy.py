"""
Imprimeix tots els nombres enters divisibles per 3 que hi ha entre A i B (inclusiu).
L'usuari introdueix dos nombres A i B

input
10
22

output
12
15
18
21
"""

A = int(input())
B = int(input())
llista = []

for x in range(A, B):
    div = True
    if x % 3 != 0:
        div = False
    if div:
        llista.append(x)

print(llista)
