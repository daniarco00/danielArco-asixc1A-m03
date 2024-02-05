a = 0
while a!=9:
    a=a+1
    for x in range(1, 10):
        if x * a < 10:
            print(x * a, end="  ")
        else:
            print(x * a, end= "  ")
        print()