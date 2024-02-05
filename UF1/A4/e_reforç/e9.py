try:


    base = int(input())
    exponent = int(input())
    potencia = 1
    for i in range(1, exponent+1):
            potencia *= base

    print(potencia)



except:
    print("Error")