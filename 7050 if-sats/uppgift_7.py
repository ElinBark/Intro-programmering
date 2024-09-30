månad = str(input("Vilken månad är du född i? "))
if månad == 'december' or månad == 'januari' or månad == 'februari':
    print('Du är född under vintern.')
elif månad == 'mars' or månad == 'april' or månad == 'maj':
    print('Du är född under våren.')
elif månad == 'juni' or månad == 'juli' or månad == 'augusti':
    print('Du är född under sommaren.')
elif månad == 'september' or månad == 'oktober' or månad == 'november':
    print('Du är född under hösten.')
else:
    print("Inte giltig månad, skriv med små bokstäver!")