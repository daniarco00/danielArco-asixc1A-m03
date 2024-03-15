import numeros as n

def introducirNumeros(): # Función que pide al usuario que introduzca un numeros en una lista
    numeros = []
    entrada = input()
    for num in entrada:
        numeros.append(num)
    return numeros

def imprimir_numeros(numeros):
    for i in numeros:
        if i in n.NUMEROS:
            print(n.NUMEROS[i])

# Ejemplo de uso
numeros = introducirNumeros()
imprimir_numeros(numeros)