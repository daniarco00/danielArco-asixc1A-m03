print("haz un programa que calcule la media de 5 notas y de la respuesta con dos decimales")

notas_str = input("Introduce las 5 notas de la UF, para saber la mediana. Separadas en , : ")
notas = notas_str.split(',')

if len(notas) != 5:
    print("Tienes que introducir 5 notas separadas por comas.")
else:
    notas = [float(nota) for nota in notas]
    media = sum(notas) / 5
    print(f"Tu media es de {media:.2f}")

