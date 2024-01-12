
try:
    dies_setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]
    dias_setmana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Fryday", "Saturday", "Sunday"]

    numero = int(input(""))

    if numero > 7 or numero < 1:
        raise TypeError

    for num in range(1,8):
        if num == numero:
            num -= 1
            print(dies_setmana[num])
            print(dias_setmana[num])
            print(days_week[num])

except:
    print("Escriu un numero del 1-7")