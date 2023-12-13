
interval = []
llista_dins_interval = []
llista_fora_interval = []
llista_igual_interval = []

limit_inferior = int(input("Introduce el limite inferior: "))
limit_superior = int(input("Introduce el limite superior: "))
while limit_superior < limit_inferior:
    limit_inferior = int(input())
    limit_superior = int(input())
for x in range(limit_inferior, limit_superior+1):
    interval.append(x)

num = 1
while num != 0:
    num = int(input("Introduce los valores: \n 0 para salir"))
    if num in interval:
        llista_dins_interval.append(num)
    elif num not in interval:
        llista_fora_interval.append(num)
    elif num == limit_inferior or limit_superior:
        llista_igual_interval.append(x)

print(f"El numero dins del interval son {sum(llista_dins_interval)} fora del interval son {llista_fora_interval}"
        f"i els que son iguals als limits d'interval son {llista_igual_interval}")

