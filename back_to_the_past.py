inheritance = float(input())
year_of_death = int(input())

years = 18

for i in range (1800, year_of_death + 1):
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= (12000 + 50 * years)
    years += 1

if inheritance < 0 :
    inheritance1 = abs(inheritance)
    print(f'He will need {inheritance1:.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.')