"""
Daniel
"""
# region Obtenir equips
def obtenir_equips():
        equipoA = input()
        equipoB = input()
        print(f"{equipoA}\n{equipoB}")
#endregion

# region Obtenir puntuacions
def obtenir_puntuacions():
    puntuacionA = 0
    while puntuacionA != -1:
        puntuacionA = [int(i) for i in input().split()]
        llistaA.append(puntuacionA)
        llistaB.append(puntuacionA[0])
#endregion

#region Processar puntuacions
#endregion
#region Dir Guanyador
#endregion

llistaA = []
llistaB= []
obtenir_equips()
obtenir_puntuacions()
print(llistaA)
print(llistaB)