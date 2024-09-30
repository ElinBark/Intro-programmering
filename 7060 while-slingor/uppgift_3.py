antal = int(input("Ange hur många tal du vill ha i fibonacci-talföljden: "))
gräns = int(input('Ange övre gänst för fibonacci-talföljden: '))
första, andra = 1, 1
i = 0
print('De första', antal, 'talen i fibonacci sekvensen är:')
while i < antal and första < gräns:
    print(första, end = ', ')
    första, andra = andra, första + andra
    i = i + 1

    if i > 0:
        print('kvot: ', format(andra/första,'.6'))


