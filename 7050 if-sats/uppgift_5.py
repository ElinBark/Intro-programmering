första = float(input("Ange ett tal: "))
andra = float(input("Ange ett till tal: "))
tredje = float(input("Ange ett tredje tal: "))
if första < andra and första < tredje:
    print(första, 'är minst')
elif andra < första and andra < tredje:
    print(andra, 'är minst')
elif tredje < första and tredje < andra:
    print(tredje, 'är minst')
elif första == andra and första < tredje:
    print(första, 'är minst')
elif första == tredje and första < andra:
    print(första, 'är minst')
elif andra == tredje and andra < första:
    print(andra, 'är minst')
else:
    print('talen är lika stora')