"""
Daniel
"""

# region Obtenir equips
def obtenir_equips():
        equipoA = input()
        equipoB = input()
        equipA.append(equipoA)
        equipB.append(equipoB)
#endregion

# region Obtenir puntuacions
def obtenir_puntuacions():
    valor = 0
    while valor != -1:
        valor = [int(i) for i in input().split()]
        if len(valor) == 2:
            llistaA.append(valor[0]), llistaB.append(valor[1])
        else:
            return valor == -1
#endregion

# region Traduir puntuaions
def traduir_puntuacions():
    for i in range(0, len(llistaA)):
        if llistaA[i] == 1:
            llistaresultatsA.append(f"Tiro libre de {equipA[0]}")
            guanyadorA.append(llistaA[i])
            return f"Tiro libre de {equipA[0]}"
        elif llistaB[i] == 1:
            llistaresultatsB.append(f"Tiro libre de {equipB[0]}")
            guanyadorB.append(llistaB[i])
            return f"Tiro libre de {equipB[0]}"
        elif llistaA[i] == 2:
            llistaresultatsA.append(f"Cistella de {equipA[0]}")
            guanyadorA.append(llistaA[i])
            return f"Cistella de {equipA[0]}"
        elif llistaB[i] == 2:
            llistaresultatsB.append(f"Cistella de {equipB[0]}")
            guanyadorB.append(llistaB[i])
            f"Cistella de {equipB[0]}"
        elif llistaA[i] == 3:
            llistaresultatsA.append(f"Triple de {equipA[0]}")
            guanyadorA.append(llistaA[i])
            return f"Triple de {equipA[0]}"
        elif llistaB[i] == 3:
            llistaresultatsB.append(f"Cistella de {equipB[0]}")
            guanyadorB.append(llistaB[i])
            return f"Triple de {equipB[0]}"
#endregion

equipA = []
equipB = []

llistaA = []
llistaB = []

llistaresultatsA = []
llistaresultatsB = []

guanyadorA = []
guanyadorB = []

obtenir_equips()
obtenir_puntuacions()
traduir_puntuacions()
