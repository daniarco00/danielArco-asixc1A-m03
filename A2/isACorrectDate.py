dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
any = int(input("Introduce el año: "))

# Verificar si la fecha es válida
if 1 <= mes <= 12:
    if mes == 2:
        if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
            max_dia = 29
        else:
            max_dia = 28
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dia = 31
    else:
        max_dia = 30

    if 1 <= dia <= max_dia:
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
else:
    print("La fecha no es válida.")