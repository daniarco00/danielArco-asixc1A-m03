"""
Daniel Arco
ASIXc M03-UF1 A3 Estructures de selecció
Introdueix el número de persones i el número de galetes.
Si a tothom li toquen el mateix número de galetes imprimeix "Let's Eat!", sinó imprimeix "Let's Fight"
Input
10 20
Output
Let's Eat!
"""

num = input()

num = num.split(" ")

num_personas = num[:1]
num_galetes = num[1:2]

if num_personas % num_galetes:
    print("it works")


