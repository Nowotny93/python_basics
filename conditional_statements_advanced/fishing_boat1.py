budget = int(input())
season = str(input())
fishers_count = int(input())

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fishers_count <= 6:
    rent = rent - rent * 0.10
elif 7 <= fishers_count <= 11:
    rent = rent - rent * 0.15
elif fishers_count >= 12:
    rent = rent - rent * 0.25

if fishers_count % 2 == 0 and season != 'Autumn':
    rent = rent - rent * 0.05

if budget >= rent:
    money_left = budget - rent
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    needed_money = rent - budget
    print(f'Not enough money! You need {needed_money:.2f} leva.')
