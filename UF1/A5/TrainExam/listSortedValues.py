n = int(input())
list = list(map(int, input().split()))
print(list)
aux = 0
while aux != 6:
    if list[aux] <= list[aux+1]:
        if aux == 3:
            print("ordenats")
            aux = 6
        else:
            aux += 1
    else:
        print("desordenats")
        aux = 6


