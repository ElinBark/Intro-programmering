första = int(input("Mata in ett heltal: "))
andra = int(input("Mata in ett till heltal: "))
tredje = int(input("Mata in ett tredje heltal: "))
if första < andra and andra < tredje:
    print(första, andra, tredje)
elif första < tredje and tredje < andra:
    print(första, tredje, andra)
elif andra < första and första < tredje:
    print(andra, första, tredje)
elif andra < tredje and tredje < första:
    print(andra, tredje, första)
elif tredje < andra and andra < första:
    print(tredje, andra, första)
elif tredje < första and första < andra:
    print(tredje, första, andra)

elif första == andra and första < tredje:
    print(första, andra, tredje)
elif första == tredje and första < andra:
    print(första, tredje, andra)
elif andra == tredje and andra < första:
    print(andra, tredje, första)

elif första == andra and första > tredje:
    print(tredje, första, andra)
elif första == tredje and första > andra:
    print(andra, första, tredje)
elif andra == tredje and andra > första:
    print(första, andra, tredje)
else:
    print(första, andra, tredje)