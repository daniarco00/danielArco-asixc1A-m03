"""
Piramide centrica
"""

piramide = int(input("Introduce el la altura la cual deseas la piramide: "))
espacio = 4

for i in range(1, piramide+1):
    print(f"{' ' * espacio}{'🧱' * i}")
    espacio -= 1