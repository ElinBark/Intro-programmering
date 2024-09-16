tal = float(input('Ange ett tal: '))
if tal >= 0 and tal < 10:
    print(tal, 'är ett ensiffrigt tal')
elif tal >= 10 and tal < 100:
    print(tal, 'är ett tråsiffrigt tal')
elif tal >= 100 and tal <= 999:
    print(tal, 'är ett tresiffrigt tal')
elif tal > 999:
    print(tal, 'är minst ett fyrsiffrigt tal')
else:
    print(tal, 'är ett negativt tal')
