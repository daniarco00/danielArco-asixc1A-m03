saliri_base = float(input("Introdueix el salari base del venedor: "))
venta_a = float(input("Introdueix el valor del primer producte venut: "))
venta_b = float(input("Introdueix el valor del segon producte venut: "))
venta_c = float(input("Introdueix el valor del tercer producte venut: "))

import_vendes = (venta_a + venta_c + venta_b) * 0.1
salari_total = saliri_base + import_vendes


print("L'import conseguit de les vendes es un total de",import_vendes,"i el salari total del venedor es",salari_total)

