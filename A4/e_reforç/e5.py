try:
    lletra = 'b'
    while lletra != " ":
        lletra = input()
        lletra = lletra.upper()
        if lletra == 'A' or lletra == 'E'or lletra == 'I' or lletra == 'O' or lletra == 'U':
            print("VOCAL")
        elif lletra == " ":
            continue
        else:
            print("NO VOCAL")


except:
    print("Error")
