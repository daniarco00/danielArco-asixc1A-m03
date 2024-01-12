
try:
    dies_setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]
    numero = int(input(""))

    if numero > 7:
        raise TypeError

    for num in range(0,8):
        if num == numero:
            num -= 1
            print(dies_setmana[num])

except:
    print("Escriu un numero del 1-7")