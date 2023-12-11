PWD = "asdasd"

clave = input("Dime la clave: ")
intento = 0


while clave != PWD and intento < 2 and clave != '1234':
    print("Clave incorrecta!!!")
    clave = input("Dime la clave:")
    intento = intento + 1

print("Bienvenido")
print("Programada terminado")




#Programa que demana a l'usuari un PIN, de manera repetitiva mentre que no introdueixi “1234”.

#L'usuari té només 3 intents.

#Quan finalment escrigui el PIN correcte, li dirà “Benvingut” i acabarà el programa.

#O quan s'esgoti el nombre d'intents, també haurà d'acabar , tot dient "LAS CAGAO BACALAO"