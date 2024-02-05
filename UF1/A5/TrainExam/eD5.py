agenda = {}
salida = True

opcions = int(input("Escogeix la operacio a realitzar. \n"
                    "1. Afegir/Modificar\n"
                    "2, Buscar\n"
                    "3. Esborrar\n"
                    "4. Llistar\n"
                    "- "))
while salida == True:
    if opcions == 1:
        clau = str(input("Introdueix el nom: "))
        if clau in agenda:
            print("Aquest contacte ja esta a la agenda.")
            print(agenda[clau])
            opcio = str(input("Vols modificarlo? S/N \n"
                              "- "))
            if opcio == 'S':
                agenda[clau] = input("Torna a introduir el numero de telefon: ")
        else:
            agenda[clau] = input(f"Introdueix el numero de telefon del contacte: ")
            print(agenda)
