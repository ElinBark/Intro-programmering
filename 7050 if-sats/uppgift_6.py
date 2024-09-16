första = int(input("Mata in ett heltal: "))
andra = int(input("Mata in ett till heltal: "))
tredje = int(input("Mata in ett tredje heltal: "))
if första < (andra and tredje) and andra < tredje:
    print(första, andra, tredje)
elif första < (andra and tredje) and tredje < andra:
    print(första, tredje, andra)
