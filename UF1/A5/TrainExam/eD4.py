n = int(input("Introdueix la quantitat d'alumnes del qual s'introduiren notes: "))
diccionari = {}
mitjana = {}
mitjana_def = {}

sortida = 1

for i in range(n):
    nom_alumne = input("Introdueix el nom de l'alumne: ")
    nota = [float(x) for x in input("Introdueix la nota o les notes del alumne: ").split()]
    diccionari[nom_alumne] = nota
    mitjana[nom_alumne] = nota

for alumne in mitjana:
    nota_mitjana = sum((mitjana[alumne])) / len(mitjana[alumne])
    mitjana_def[alumne] = nota_mitjana

print(diccionari)
print(mitjana_def)