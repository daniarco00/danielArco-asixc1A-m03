print("Benvolgut al calculador de la nota final de programació. Introdueix els valors necessaris per calcular-la.")

qualificio_a = float(input("Introdueix la nota de la primera de les proves: "))
qualificio_b = float(input("Introdueix la nota de la segona de les proves: "))
qualificio_c = float(input("Introdueix la nota de la tercera de les proves: "))
nota_prova = float(input("Introdueix la nota de la prova final: "))
nota_treball = float(input("Introdueix la nota del treball final: "))

mitjana_qualificacions = ((qualificio_a + qualificio_b + qualificio_c) / 3) * 0.55
mitjana_prova = nota_prova * 0.3
mitjana_treball = nota_treball * 0.15

nota_final = mitjana_treball + mitjana_prova + mitjana_qualificacions

print("La teva nota final es",nota_final)