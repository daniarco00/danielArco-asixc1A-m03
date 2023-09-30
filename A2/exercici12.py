import math

x1 = float(input("Ingresa el valor del primer punt pla de x: "))
x2 = float(input("Ingresa el valor del segon punt pla de x: "))

y1 = float(input("Ingresa el valor del segon punt pla: "))
y2 = float(input("Ingresa el valor del segon punt pla de y: "))

distancia_AB = math.sqrt((x2 - x1)**2)+((y2- y1)**2)


print(f"La distancia entre els dos punts es:  {distancia_AB}")