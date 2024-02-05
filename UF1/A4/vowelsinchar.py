"""


Programa que calcula el factorial d'un número n. El factorial de n, n!= n * n-1*n-2*….*3*2*1


"""

vowels = 'aeiou'


caracters = input()

for char in caracters:
    if char.lower() in vowels:
        print(char, end="")
