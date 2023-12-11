try:

    num = 1
    llista = []
    cont = 0
    while num != 0:
        num = int(input())
        cont += 1
        llista.append(num)
    print(f"La suma de tots el numero introduits es {sum(llista)} i la mitjana es {sum(llista)/cont}")


except:
    print("error")