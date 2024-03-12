from read import entrada_usuari, seleccio_color, definir_largaria, definir_ancho, imprimir_forma
from color import CRED, CBLUE, CGREEN


if __name__ == "__main__":
    cuadrat = entrada_usuari()
    color = seleccio_color(cuadrat)
    largaria = definir_largaria(cuadrat)
    ancho = definir_ancho(cuadrat)
    imprimir_forma(color, largaria, ancho)




