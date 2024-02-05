

user_input = 0
password = 'patata'
attemps = 3
while user_input != 'patata':
    if attemps > 0:
        user_input = input("Password: ")
        password = user_input
        attemps = attemps - 1
    else:
        print("Has superado el límite de intentos.")
        break