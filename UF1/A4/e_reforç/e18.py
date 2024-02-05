import time
hora = 0
minuto = 0
segundo = 0


while True:
    print(f"´{hora:02}:{minuto:02}:{segundo:02}")
    segundo += 1
    time.sleep(0.15)

    if segundo == 60:
        segundo = 0
        minuto += 1

    if minuto == 60:
        minuto = 0
        hora += 1

    if hora == 24:
        hora = 0




