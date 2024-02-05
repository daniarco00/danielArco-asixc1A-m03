"""Separa todos los digitos de un numero, para posteiormente sumarlos todos entre si"""

n = int(input())
suma_digitos = sum(int(digito) for digito in str(n))
print(suma_digitos)
