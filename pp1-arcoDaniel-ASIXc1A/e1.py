import math

print("Programa que mostra per pantalla l'àrea i el volum d'una piràmide quadrangular. ")

altura = float(input("Introdueix l'alçada de la piramide (en cm): "))
costat = float(input("Introdueix la mida dels costats de la piramide (en cm): "))


area = costat * (costat + math.sqrt(4*(altura*altura) + (costat * costat)))
volum = ((costat * costat) * altura) / 3

print(f"El volum de la piràmide quadrangular serà de {volum:.2f}cm³ i l'àrea serà de {area:.2f}cm².")








