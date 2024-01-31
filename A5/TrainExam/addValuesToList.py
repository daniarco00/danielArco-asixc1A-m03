import random

llista = [float(random.randint(0.0, 0.0)) for i in range(50)]

llista[0] = float(input("primera: "))
llista[1] = float(input("segona: "))
llista[19] = float(input("vintena: "))
llista[-1] = float(input("ultima: "))

print(llista)