

diccionari_insults = {
    "CAT": ("Mocos", "Capgros", "Capdesuru", "Capsigrany", "Camacurt", "PASTANAGA", "GAMARUS"),
    "ESP": ("Mocoso", "Feo", "Cabezón", "Pata sucia", "Tonto", "Zanahoria", "GAMARUS"),
    "ENG": ("Booger", "Ugly", "Big head", "Dirty foot", "Fool", "Carrot", "GAMARUS"),
    "KLG": ("qo'", "nuch", "mIQ", "QI'lop", "bIQ", "Qargh", "GAMARUS")
}

insult = input("Introudiex un insult en catala: ")
cont = 0
for i in diccionari_insults["CAT"]:
    if insult == i:
        print(f"Insult en Castella: {diccionari_insults['ESP'][cont]}")
        print(f"Insult en Angles: {diccionari_insults['ENG'][cont]}")
        print(f"Insult en Klinton: {diccionari_insults['KLG'][cont]}")
    else:
        cont += 1