första = float(input("Ange ett tal: "))
andra = float(input("Ange ett till: "))
if första > andra:
    print(första, "är det största talet")
elif första == andra:
    print("talen är lika stora")
else: 
    print(andra, "är det största talet")