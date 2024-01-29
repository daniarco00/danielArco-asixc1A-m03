import random

llista = [random.randint(1,50) for i in range(100)]
parell = []
senar = []
sum_parell = 0
sum_senar = 0

for i in range(100):
    if i % 2 == 0:
        parell.append(llista[i])
        sum_parell += llista[i]
    else:
        senar.append(llista[i])
        sum_senar += llista[i]

print(f"Amb els nombres: {llista}\n"
      f"mitjana posicions parelles: {sum_parell / len(parell)}\n"
      f"mitjana posicions senars: {sum_senar / len(senar)}")