"""
Implementa un programa que demani un número i calculi el seu factorial .
El factorial d'un nombre és el producte de tots els enters entre 1 i el mateix nombre i es representa pel nombre seguit
 d'un signe d'exclamació. Per exemple 5! = 1x2x3x4x5= 120)
"""


try:
    n = int(input("Ingrese un número: "))

    factorial = 1

    for x in range(1, n + 1):
        factorial *= x

    print(f"El factorial de {n} es: {factorial}")

except ValueError:
    print("Error: Ingrese un número válido.")
except Exception as e:
    print(f"Error: {e}")

