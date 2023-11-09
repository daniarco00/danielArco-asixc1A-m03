hora_actual = input("Introdueix la hora en hores minuts i segons separats per espais respectivament: ")
hora_actual = hora_actual.split()


if int(hora_actual[0]) >= 24 and int(hora_actual[1]) >= 59:
    int(hora_actual[2]) + 1
    print(f"")


#elif int(hora_actual[0]) <= 24 and int(hora_actual[1]) < 59:
#    int(hora_actual[1]) + 1








