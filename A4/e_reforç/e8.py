try:
    llista = []
    llista_interval = []
    llista_forainterval = []
    llista_restant = []
    num = 1

    interval_alt = int(input())
    interval_baix = int(input())
    """while interval_alt < interval_baix:
        interval_baix = int(input())
        interval_alt = int(input())"""

    for i in range(interval_baix, interval_alt+1):
        llista.append(i)
    while num != 0:
        num = int(input())
        if num == interval_baix or num == interval_alt:
            llista_restant.append(num)
        elif num not in llista:
            llista_interval.append(num)
        elif num in llista:
            llista_forainterval.append(num)

    print(f"La suma dels numeros que estan dins del interval es {sum(llista_interval)}. \n"
          f"La quantitat de numeros que son fora del interval son {llista_forainterval}. \n"
          f"Hi han hagut tants {len(llista_restant)}.")


except:
    print("Error")
