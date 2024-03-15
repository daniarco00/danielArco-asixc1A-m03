from color import CRED, CBLUE, CGREEN
#region Entrada de dades
def entrada_usuari():
    sortida = ''
    cuadrat = []
    while True:
        sortida = input('')
        if sortida == ';Q':
            break
        cuadrat.append(sortida.split())
    return cuadrat

#endregion
#region Selecció de color
def seleccio_color(cuadrat):
    color = []
    for i in range(len(cuadrat)):
        if cuadrat[i]:  # Comprobar si la sublista tiene al menos un elemento
            cuadrat[i][0] = cuadrat[i][0].upper()
            if cuadrat[i][0] == 'RED':
                color.append(CRED)
            elif cuadrat[i][0] == 'BLUE':
                color.append(CBLUE)
            elif cuadrat[i][0] == 'GREEN':
                color.append(CGREEN)
    return color
#endregion
#region definir largaria
def definir_largaria(cuadrat):
    largaria = []
    for i in range(len(cuadrat)):
        largaria.append(int(cuadrat[i][1]))
    return largaria
#endregion
#region definir ancho
def definir_ancho(cuadrat):
    ancho = []
    for i in range(len(cuadrat)):
        ancho.append(int(cuadrat[i][2]))
    return ancho
#endregion
#region imprimir forma
def imprimir_forma(color, largaria, ancho):
    for i in range(len(color)):
        for _ in range(ancho[i]):
            print(color[i] + 'X'*largaria[i])
        print()
#endregion
