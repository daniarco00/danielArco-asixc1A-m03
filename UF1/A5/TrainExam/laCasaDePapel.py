claves = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

entrada = list(map(int, input().split()))

for i in entrada:
    if i != -1:
        claves[i] += 1

print(claves)
