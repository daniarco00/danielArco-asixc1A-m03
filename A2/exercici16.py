print("[+] La velocitat del vehicle B ha de ser més alta que la del vehicle A.")
vB = float(input("Introdueix la velocitat en km/h a la que va el vehicle B: "))
vA = float(input("Introdueix la velocitat en km/h a la que va el vehicle A: "))
if vA >= vB:
    print("Has introduït les dades incorrectament.")
    exit(1)

distancia = float(input("Introdueix la distancia a la qual esta el vehicle B del A: "))

vB_final = (vB * 1000) / 3600
vA_final = (vA * 1000) / 3600


t = ((vB_final * distancia) - (vA_final * distancia)) / 60

print(f"El cotxe B tardarà {t} en alcanzar a cotxe A")



