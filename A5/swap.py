

entrada_usuario = input()
llista = entrada_usuario.split()

primer = llista[0]
ultim = llista[-1]

llista[0] = ultim
llista[-1] = primer

print(llista)