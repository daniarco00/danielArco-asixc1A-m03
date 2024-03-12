import random
import re

def solicitar_frase():
    return input("Introduce una frase: ")


def desordenar_palabras(frase):
    urls = re.findall(r'(http://)[^\s]*', frase)
    for url in urls:
        frase = frase.replace(url, '{}')
    palabras = re.split('([^a-zA-Z0-9áéíóúÁÉÍÓÚ])', frase)
    resultado = []
    for palabra in palabras:
        if palabra.isdigit() and len(palabra) == 9:
            nueva_palabra = palabra
        elif len(palabra) > 2 and (palabra[0].isalnum() and palabra[-1].isalnum()):
            first_char = palabra[0]
            last_char = palabra[-1]
            centro = list(palabra[1:-1])
            random.shuffle(centro)
            nueva_palabra = first_char + ''.join(centro) + last_char
        else:
            nueva_palabra = palabra
        resultado.append(nueva_palabra)
    frase_randomizada = ''.join(resultado).format(*urls)
    return frase_randomizada


frase = solicitar_frase()
print(desordenar_palabras(frase))