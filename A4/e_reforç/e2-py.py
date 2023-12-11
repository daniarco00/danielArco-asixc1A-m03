import random
try:
    intents = 0
    num = random.randint(1, 100)
    print(num)

    while intents != 10:
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