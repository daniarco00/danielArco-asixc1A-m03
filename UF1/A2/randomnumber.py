import random
import math

lower = int(input("Introduce el rango de numero minimo con el que quieres jugar: "))

upper = int(input("Introduce el rango del numero maximo con el que quieras jugar: "))


x = random.randint(lower, upper)
vidas = 3


for intento in range(1, 4):
    response1 = int(
        input("Tu numero aleatorio se ha generado. Tienes 3 intentos para adivinarlo. Introduce aqui tu primera "
                  "respuesta: "))

    if response1 == x:
        print("Genial has adivinado el numero!")
    elif response1 < x:
        print("El numero aleatorio es mas grande al numero que has introducido. :p")
        vidas -= 1
    elif response1 > x:
        print("El numero aleatorio es mas pequeño al que has introducido. ;)")
        vidas -= 1
    if vidas == 0:
        print("Te has quedado sin vidas. :(")
        break


