moneda_05=int(input("Cuantas monedes de 0,05 centims tens? "))
moneda_10=int(input("Cuantas monedes de 10 centims tens? "))
moneda_20=int(input("Cuantas monedes de 20 centims tens? "))
moneda_50=int(input("Cuantas monedes de 50 centims tens? "))
moneda_1=int(input("Cuantas monedes de 1€ tens? "))
moneda_2=int(input("Cuantas monedes de 2€ tens? "))

total_05=0.05*moneda_05
total_10=0.10*moneda_10
total_20=0.20*moneda_20
total_50=0.50*moneda_50
total_1=moneda_1*1
total_2=moneda_2*2

quantitat_total=total_2+total_1+total_05+total_10+total_20+total_50

print("El resultado es {:.2f}".format(quantitat_total))