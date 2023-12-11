try:
    num1 = int(input())
    num2 = int(input())
    llista_parells = []
    llista_senars = []

    for x in range(num1, num2):
        if x % 2 == 0:
            llista_parells.append(x)
        else:
            llista_senars.append(x)

    print(f"Els nombres parells son {llista_parells}, i els imparells son {llista_senars}")
except:
    print("Error")
