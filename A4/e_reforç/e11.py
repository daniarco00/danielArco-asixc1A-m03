"""Escriu un programa que digui si un número introduït per teclat és primer o no. Un nombre primer és aquell que només
és divisible entre ell mateix i la unitat.
Ajuda: Donat un número, és suficient provar tots els números entre 2 i l'arrel quadrada del número en qüestió per veure
 si aquest és primer o no."""


num = int(input())
llista = []

for x in range(1, num+1):
    if num % x == 0:
        llista.append(x)
    else:
        continue

if sum(llista) == 1+num:
    print(f" {num} és un nombre primer")
else:
    print(f" {num} no és un nombre primer")