llista_senseIVA = list(map (int, input().split()))
llista_ambIVA = []
for i in range(len(llista_senseIVA)):
    calculIVA = (llista_senseIVA[i]*0.21) + llista_senseIVA[i]
    llista_ambIVA.append(calculIVA)

for i in range(len(llista_senseIVA)):
    print(f"{llista_senseIVA[i]} = {llista_ambIVA[i]}")
