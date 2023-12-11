import time
while True:
    hora = 00
    minuto = 00
    segundo = 00
    print(f"{hora}:{minuto}:{segundo}")
    for i in range(1, 60):
        segundo += 1
        print(f"{hora}:{minuto}:{segundo}")
        time.sleep(0.1)
    if i == 59:
        segundo == 0
        minuto += 1
        print(f"{hora}:{minuto}:{segundo}")
        time.sleep(0.1)
        for i in range(1, 60):
            segundo += 1
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(0.1)






