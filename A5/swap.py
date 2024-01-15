
llista = []
llista = (input())

primer = llista[0]
ultim = llista[:-1]

print(llista[0])
print(primer)


llista[0:] = ultim
llista[:-1] = primer


print(llista)