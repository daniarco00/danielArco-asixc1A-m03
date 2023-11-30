
n = int(input())
if n <= 256:
    binario = bin(n)[2:]
    print(binario)
else:
    print("Numero incorrecto")