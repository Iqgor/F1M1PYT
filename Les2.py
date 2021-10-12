def start():
    a = "firetruck"
    b = " a "
    print(a[0:1] + a[6:9] + b + a[4:9])
    print('Hou je van trucks?y/n')

    option = input("")
    if option.lower() == 'y':
        print('Oke fuck a duck!')
        start()
    if option.lower() == 'n':
        exit()
start()