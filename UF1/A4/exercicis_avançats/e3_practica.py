nums[0] = int(input("Introdueix la alçada que ha de tenir el tringle (entre 2-9): "))

for x in range(1, nums[0]+1):
    if x == 1:
        print(x)
    elif 1 < x < nums[0]:
        print(f"{x}{' ' * (x)}{x}")
    elif x == nums[0]:
        valor = str(x) + " "
        print(f"{valor * x}")



