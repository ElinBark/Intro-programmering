gissningar = 0
while gissningar < 3:
    gissningar += 1
    tal = int(input('Mata in ett tal: '))
    while tal != 42:
        if tal < 42:
            print('för litet')
        elif tal > 42:
            print('för stort')
        tal = int(input('gissa igen: '))
    print('Rätt!')


    gissningar = 0
while gissningar < 3:
    tal = int(input('Mata in ett tal: '))
    gissningar = gissningar + 1

    while tal != 42:
        if tal < 42:
            print('för litet')
            tal = int(input('gissa igen: '))
        elif tal > 42:
            print('för stort')
            tal = int(input('gissa igen: '))
    print('Rätt!')


    gissningar = 0
while gissningar < 3:
    tal = int(input('Mata in ett tal: '))
    gissningar = gissningar + 1

    if tal == 42:
        print('Rätt!')
    elif tal < 43:
        print('för litet')
        tal = int(input('gissa igen: '))
    else:
        print('för stort')
        tal = int(input('gissa igen: '))