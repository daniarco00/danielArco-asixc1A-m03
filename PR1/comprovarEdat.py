"""
Procs: major_edat
"Digues-e la teva edat"
Llegir edat;
si edat>= 18 llavors
    Escriure ets major d'edat
FinSi
Escriure "Programa acabat"

"""

#Programa que et demana l'edat i diu si ets major d'edat.
edat = int(input("Quina edat tens? "))

if edat >= 18:
    print("Ets major d'edat")
else:
    print("No ets major d'edat")
    exit(0)

