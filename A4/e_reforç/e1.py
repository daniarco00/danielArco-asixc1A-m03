
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
