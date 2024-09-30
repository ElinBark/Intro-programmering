
gissningar = 0
while gissningar < 3:
    gissningar = gissningar + 1
    tal = int(input('Mata in ett tal: '))

    while tal != 42:
        if tal < 42:
            print('för litet')
            tal = int(input('gissa igen: '))
        elif tal > 42:
            print('för stort')
            tal = int(input('gissa igen: '))
    print('Rätt!')

    if gissningar == 3:
        print('Du har slut på gissningar')
