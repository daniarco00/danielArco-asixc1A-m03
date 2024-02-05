"""
Fer un programa que dibuixa un avet del Canadà.
Cal demanar la mida de l'arbre. La mida inclou el tronc i les branques
"""

hoja = "🌿"
n = int(input())

for i in range(1, n+1):
    if i >= 0.8 * n:
        espais_tronc = " " * (int((0.8 * n)))
        amplada_tronc = "🏾" * int((0.2 * n))
        print(f"{espais_tronc}{amplada_tronc}")
    else:
        espacio = " " * (n - i)
        bricks = hoja * i
        print(espacio + bricks)