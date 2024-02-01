"""Descripció: Implementar un programa que faci les següents operacions:
Demanar, a l'usuari, la quantitat de files i columnes d'una matriu 2D.
Comprovar que la matriu sigui quadrada, es a dir que tingui les mateixes fileres que columnes
Guarda la matriu en una variable anomenada "matriu"
Omplir la matriu amb 1's a les vores i la resta amb 0's.
La mida de la matriu a de ser senar"""

nums = [int(i) for i in input().split()]

if nums[0] == nums[1] and nums[0] % 2 != 0 and nums[1] % 2 != 0:
    matriu = [[0] * nums[0] for j in range(nums[1])]
    for i in range(nums[0]):
        for j in range(nums[1]):
            if i == 0 or j == nums[1]-1 or j == 0 or i == nums[0]-1:
                matriu[i][j] = int(1)
    for x in matriu:
        print(x)
else:
    print("Els numeros no son iguals o no es senar.")


