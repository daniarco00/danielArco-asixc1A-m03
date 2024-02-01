"""
Descripció:Encriptar frases:
Fer un programa per llegir una frase pel teclat i, en acabar, mostri la frase encriptada.
Per encriptar la frase, ha de fer servir el valor numeric de cada lletra. Caldrà escriure un punt "." per
poder indentificar a on comença i acaba cada lletra.
"""

entrada = [str(x) for x in input()]

print(entrada)
frase_encriptada = []
for i in entrada:
    encriptacio = ord(i)
    frase_encriptada.append(encriptacio)


contador = 0
print(len(frase_encriptada))
for x in frase_encriptada:
    if (len(frase_encriptada)) == contador:
        print(f"{x}", end="")
    else:
        print(f"{x}.", end="")
        contador += 1
