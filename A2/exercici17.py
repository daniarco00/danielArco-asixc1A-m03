print("Tenim que un ciclista va de ciutat A a ciutat B. \nSegons els valors que m'introudeixis, Et dire l'hora d'arribada.")
t = float(input("Introdueix els segons que tarda en arribar de ciutat A a ciutat B: "))
horaPartida = input(("Ingrese la hora de partida en (formato HH:MM:SS) : "))


hora_partida_split = horaPartida.split(":")
hora_partida_horas = int(hora_partida_split[0])
hora_partida_minutos = int(hora_partida_split[1])
hora_partida_segundos = int(hora_partida_split[2])


hora_llegada_segundos = hora_partida_segundos + t
hora_llegada_minutos = hora_partida_minutos + (hora_llegada_segundos // 60)
hora_llegada_segundos = hora_llegada_segundos % 60
hora_llegada_horas = hora_partida_horas + (hora_llegada_minutos // 60)
hora_llegada_minutos = hora_llegada_minutos % 60

print(f"La hora de llegada a la ciudad B es: {hora_llegada_horas}:{hora_llegada_minutos}:{hora_llegada_segundos}")
