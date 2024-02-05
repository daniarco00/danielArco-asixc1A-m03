extern = int(input("Introdueix la mida dels costats quadrat extern: "))
intern = int(input("Introdueix la mida dels costats quadrat intern: "))

exit = 1

for i in range(1, extern+1):
    if i == intern:
        for j in range(1, intern+1):
            print(f"{'*' * ((extern - intern) // 2)}", end="")
            print(f"{'#' * intern}", end="")
            print(f"{'*' * ((extern - intern) // 2)}", end="")
            print()
    else:
        if i == extern + 2 - intern:
            print(i)
        else:
            print(f"{'*' * extern}")


"""
extern = int(input("Introdueix la mida dels costats quadrat extern: "))
intern = int(input("Introdueix la mida dels costats quadrat intern: "))

for i in range(extern):
    for j in range(extern):
        if i < intern // 2 or i >= extern - intern // 2 or j < intern // 2 or j >= extern - intern // 2:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()
"""
