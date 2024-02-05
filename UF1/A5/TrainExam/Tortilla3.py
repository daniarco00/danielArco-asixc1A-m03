"""Descripció: Mida paraulas:
Implementar un programa que faci les següents operacions:
Crear una variable per emmagatzemar 666 paraules
Mostrar tot el seu contingut.
Omplir-la, pel teclat, amb paraules. No cal omplir-la del toto. Quan la paraula introduïda és "\q" es deixad'introduir paraules.
Calcular la llargada maxima de les paraules introduides i mostra-la per la pantalla.
Mostrar la tupla amb les paraules i mides corresponents"""

LLARGADA = 666
ESCAPE = "\q"
paraules = ['']
count = 0
while count < LLARGADA:
    entrada = (input())
    if entrada == ESCAPE:
        break
    paraules.append(entrada)
    count += 1

tuples_list = []
for paraula in paraules:
    tupla = tuple((paraula, len(paraula)))
    tuples_list.append(tupla)

print(tuples_list)

