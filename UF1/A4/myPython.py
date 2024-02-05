<<<<<<< HEAD

"""
Programa per crear una serp Python a mida.
Cal demanar quina mida (quantitat de COS) ha de tenir la
serp. Tot seguit mostrar-la per pantalla.
Es valorarà el fet de que el cos faci siga sagues.
 Potser, la mida del cos ha de ser mínim 5
"""


CAP= "....\...../...."
ULLS= "...╚⊙ ⊙╝..."
COS = "═(███)═"
CUA =  " ═V═ "

mida = int(input())

if mida >= 5:
    print(CAP)
    print("  " + ULLS)
    for x in range(mida):
        print("    " + COS)

    print("     " + CUA)
else:
    print("El valor minim de cos es de 5")


=======
import math

CAP= "....\...../...."

ULLS= "...╚⊙ ⊙╝..."

COS = "═(███)═"

CUA =  " ═V═ "


valor = int(input())



print(f"{CAP}")
print(f"  {ULLS}")
for x in range(valor):
    zigzag = "     "
    contador = zigzag + "  "
    print(f"{zigzag}{COS}")

print(CUA)
>>>>>>> origin/master
