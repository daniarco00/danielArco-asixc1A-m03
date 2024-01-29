

entrada_usuario = [int(i) for i in input().split()]

primer = entrada_usuario[0]
ultim = entrada_usuario[-1]

entrada_usuario[0] = ultim
entrada_usuario[-1] = primer

print(entrada_usuario)