altura = int(input("Introdueix la alçada que ha de tenir el tringle (entre 2-9): "))

for x in range(1, altura+1):
    if x == 1:
        print(x)
    elif 1 < x < altura:
        print(f"{x}{' ' * (x)}{x}")
    elif x == altura:
        valor = str(x) + " "
        print(f"{valor * x}")



