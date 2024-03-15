import string


def introducirnumeros(): # Función que pide al usuario que introduzca un numeros en una lista
    numeros = []
    entrada = input('')
    for palabra in entrada.split():
        numeros.append(palabra)
    return numeros

def contarPalabras(palabra): # Función que cuenta las palabras de un numeros
    diccionario = {}
    for pal in palabra:
        pal = pal.translate(str.maketrans('', '', string.punctuation))
        pal = pal.lower()
        if pal:
            if pal not in diccionario:
                diccionario[pal] = 1
            else:
                diccionario[pal] += 1
    print(diccionario)
    return diccionario









