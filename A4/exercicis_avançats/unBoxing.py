costatA = int(input("introdueix la mida de les columnes: "))
costatB = int(input("introdueix la mida de les columnes: "))

for i in range(1, 2):
    print(f"{'🟫' * costatA}", end="")
    print()
    for j in range(1, costatB):
        print(f"🟫{' ' * ((costatA * 2) - 2)}🟫")
    print(f"{'🟫' * costatA}", end="")

