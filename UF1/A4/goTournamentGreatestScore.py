
puntuacions = []

while True:
    nom = str(input())
    if nom != 'END':
        punt = int(input())
        puntuacions.append((nom, punt))
    else:
        break

puntuacions_fin = max(puntuacions)
print((puntuacions_fin))


