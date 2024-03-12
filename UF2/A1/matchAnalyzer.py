"""
Daniel
"""
# region Obtenir equips
def obtenir_equips():
        equipoA = input()
        NomEquipA.append(equipoA)
        equipoB = input()
        NomEquipoB.append(equipoB)
        print(f"{equipoA}\n{equipoB}")
#endregion

# region Obtenir puntuacions
def obtenir_puntuacions():
    entrada = 0
    while entrada != -1:
        try:
            entrada = input()
            puntuacionA, puntuacionB = map(int, entrada.split())
            llistaA.append(puntuacionA)
            llistaB.append(puntuacionB)
        except:
            entrada = -1
#endregion\
#endregion


#region Processar puntuacions
def procesar_puntuacions():





#endregion



#region Dir Guanyador
#endregion

NomEquipA = []
NomEquipB = []

llistaA = []
llistaB= []

puntuacionsA = []
puntuacionsB = []

obtenir_equips()
obtenir_puntuacions()
print(llistaA)
print(llistaB)