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

try:
    entrada = input().split()
    entrada_personas = int(entrada[0])
    entrada_galetes = int(entrada[1])
    if entrada_galetes % entrada_personas == 0:


except:
    print("Las cagao")
