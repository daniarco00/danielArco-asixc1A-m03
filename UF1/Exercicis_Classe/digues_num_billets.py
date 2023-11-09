entrada = float(input())
if entrada > 500:
    primera_entrada = int(entrada / 500)
    print(f"Necessites {primera_entrada} billets de 500")
    entrada1 = entrada - (500 * primera_entrada)
else:
    print("No necessites billets de 500.")

if entrada1 > 200:
    segona_entrada = int(entrada1 / 200)
    print(f"Necessites {segona_entrada} billets de 200")
    entrada2 = entrada1 - (200 * segona_entrada)
else:
    print("No necessites bitllets de 200")

if entrada2 > 100:
    tercera_entrada = int(entrada2 / 100)
    print(f"Necessites {tercera_entrada} billets de 100")
    entrada3 = entrada2 - (100 * tercera_entrada)
else:
    print("No necessites bitllets de 100")

if entrada3 > 100:
    cuarta_entrada = int(entrada3 / 50)
    print(f"Necessites {cuarta_entrada} billets de 50")
    entrada4 = entrada3 - (50 * cuarta_entrada)
else:
    print("No necessites bitllets de 50")

if entrada4 > 20:
    quinta_entrada = int(entrada4 / 20)
    print(f"Necessites {quinta_entrada} billets de 20")
    entrada5 = entrada4 - (20 * quinta_entrada)
else:
    print("No necessites bitllets de 20")

if entrada5 > 10:
    quinta_entrada = int(entrada4 / 20)
    print(f"Necessites {quinta_entrada} billets de 20")
    entrada5 = entrada4 - (20 * quinta_entrada)
else:
    print("No necessites bitllets de 20")

