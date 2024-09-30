tal = int(input('Mata in ett tal: '))
while tal != 42:
    if tal < 42:
        print('för litet')
        tal = int(input('gissa igen: '))
    else:
        print('för stort')
        tal = int(input('gissa igen: '))
print('Rätt!')