

factura_inicial = float(input("Introdueix el valor de la factura: "))
client = input("Tens la targeta client (S/N): ")
if client.upper() == 'S' and factura_inicial >= 100:
    factura_descompte = factura_inicial * 0.79
    factura_final = factura_descompte * 1.21
    print(f'La teva factura final amb el descompte aplicat es de {factura_final:.2f}')
else:
    print(f'La teva factura final es de {factura_inicial:.2f}')

