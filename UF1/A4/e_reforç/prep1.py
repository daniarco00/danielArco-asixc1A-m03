
try:
    cadena = str(input("Introdueix la cadena: "))
    car_original = str(input("Introduce el caracter que quieres sustituir: "))
    car_remplazado = str(input("Introduce el caracter por el que lo quieres sustiruir: "))


    for char in cadena:
        if car_original in char:
            print(car_remplazado, end="")
        else:
            print(char, end="")

except ValueError:
    print("Introduce bien los datos.")