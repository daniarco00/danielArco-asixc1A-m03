"""
n = int(input())
for i in range(n):
    m = n// 2
    print(m*'#', end="")
    print(m*'#')
print()
"""
n = int(input("Ingrese la medida del cuadrado (N): "))

# Imprimir la parte superior del cuadrado
print("#" * n)

# Imprimir el cuerpo del cuadrado
for i in range(n - 2):
    print("#" + " " * (n - 2) + "#")

# Imprimir la parte inferior del cuadrado
if n > 1:
    print("#" * n)