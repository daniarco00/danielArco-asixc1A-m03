"""
e3. Programa que mostra per pantalla la suma de tots els nombres senars
 i de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
"""
x = int(input())
lista = []
lista_parells = []
lista_senars = []

for i in range(1,x):
    lista.append(i)

for j in range(lista[0], lista[-1]):
    if j % 2 == 0:
        lista_parells.append(j)
    else:
        lista_senars.append(j)

print(f"Els numeros parells son {lista_parells} i els senars {lista_senars}")






