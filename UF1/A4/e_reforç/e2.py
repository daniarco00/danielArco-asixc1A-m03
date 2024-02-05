"""
Crea una aplicació que permet endevinar un número. L'aplicació genera un nombre “aleatori” de l'1 al 100. A continuació,
 l’aplicació va demanant números i va responent si el nombre a endevinar és més gran o més petit que el que ha introduït,
 a més dels intents que et queden (tens 10 intents per encertar-lo). El programa acaba quan s'encerta el número (a més et
 diu quants intents has necessitat per encertar-lo), si s'arriba al límit d'intents, l’aplicació et mostra el número que
 havia generat.
"""

import random
try:
    intents = 1
    num = random.randint(1, 100)
    print(num)

    while intents != 10 and num != num_usuari:
        num_usuari = int(input("Introdueix el numero: "))
        if num_usuari != num:
            print("Incorrecte, torna a provar.")
            intents += 1
            if num_usuari > num:
                print("El numero es més baix")
            else:
                print("El numero es més alt")
        else:
            print(f"Correcte!, has necesitat {intents} vegades.")
            intents = 10

    if intents == 10 and num_usuari != num:
        print(f"El numero correcte era {num}.")

except:
    print("Error")