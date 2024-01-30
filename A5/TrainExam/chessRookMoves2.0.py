TABLERO = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

x = str(input())
y = int(input())
LLETRA = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

for i in range(len(TABLERO)):
    if TABLERO[i][LLETRA[x]] == 0:
        TABLERO[i][LLETRA[x]] = 1
    for j in range(len(TABLERO)):
        if TABLERO[y][j] == 0:
            TABLERO[y][j] = 1
        elif TABLERO[y][LLETRA[x]] == 1:
            TABLERO[y][LLETRA[x]] = 2

for i in range(len(TABLERO)):
    print(TABLERO[i])


