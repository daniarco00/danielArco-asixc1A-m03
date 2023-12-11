"""
Imprimir de la A fins la Z.
A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva. Fins aconseguir tenir
una linia que mostri de la A fins la Z
Output
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H 
"""


for i in range(ord("A"),ord("Z")+1):
    for j in range(ord("A"), i+1):
        print(chr(j), end="") #El end sirve para evitar la ultima linea
    print() #Salto de linea



