try:
    nums = [int(i) for i in input().split()]

    for i in range(nums[0]):
        for j in range(0, nums[1]):
            if i == 0 or j == 0:
                print("1", end="")
            elif i == nums[0]-1 or j == nums[1]-1:
               print("1", end="")
            else:
                print("0", end="")
        print()
except:
    print("Introduce bien los datos")