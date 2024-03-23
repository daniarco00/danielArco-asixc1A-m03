import numeros as n
#region Recoger numeros
def introducirNumeros(): # Función que pide al usuario que introduzca un numeros en una lista
    numeros = []
    while True:
        entrada = input()
        if entrada == ':Q':
            break
        for palabra in entrada.split():
            numeros.append(palabra)
    return numeros
#endregion
#region Imprimir numeros
def imprimir_numeros(numeros):
    output = ""
    for j in range(len(n.NUMEROS[int(numeros[0])])):
        for k in range(0, len(numeros)):
            output += n.NUMEROS[int(numeros[k])][j] + "  "
        output += "\n"
    print(output)
#endregion