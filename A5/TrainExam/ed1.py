try:
    n = int(input())

    diccionario = {}

    for i in range(1, n+1):
        valor = i * i
        diccionario[i] = valor

    for clave, valor in diccionario.items():
        if valor == n*n:
            print(f"{{{clave}:{valor}}}", end="")
        else:
            print(f"{{{clave}:{valor}}}", end=",")
except:
    print("cagao")