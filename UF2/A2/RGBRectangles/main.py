from kernel import entrada_usuari, seleccio_color, definir_largaria, definir_ancho, imprimir_forma
from color import CRED, CBLUE, CGREEN


if __name__ == "__main__":
    while True:
        cuadrat = entrada_usuari()
        if not cuadrat:  # Si la lista está vacía, significa que el usuario ingresó ;Q
            break
        color = seleccio_color(cuadrat)
        largaria = definir_largaria(cuadrat)
        ancho = definir_ancho(cuadrat)
        imprimir_forma(color, largaria, ancho)




