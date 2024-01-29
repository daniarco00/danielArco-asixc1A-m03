K = 8
K = 8
vert = input("")
horitz = int(input())
LLETRA = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

for i in range(K):
    for j in range(K):
        if i == LLETRA[vert] and j+1 == horitz:
            print(" 2 ", end="")
        elif i == LLETRA[vert]:
            print(" 1 ", end="")
        elif j+1 == horitz:
            print(" 1 ", end="")
        else:
            print(" X ", end="")
    print()