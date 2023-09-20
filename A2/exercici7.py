print("Benvolgut al conversor de minuts a hores.")
quantitat_min = int(input("Introdueix la quantitat de minuts que vulgui convertir: "))


hores = quantitat_min // 60
minuts_residu = quantitat_min % 60

print(f"Son un total de",hores,"i",minuts_residu)

