type_flowers = str(input())
number_flowers = int(input())
budget = int(input())

if type_flowers == 'Roses':
    if number_flowers > 80:
        price_roses = number_flowers * 5 - (number_flowers * 5) * 0.1
    else:
        price_roses = number_flowers * 5
elif type_flowers == 'Dahlias':
    if number_flowers > 90:
        price_dahlias = number_flowers * 3.80 - (number_flowers * 3.80) * 0.15
    else:
        price_dahlias = number_flowers * 3.80
elif type_flowers == 'Tulips':
    if number_flowers > 80:
        price_tulips = number_flowers * 2.80 - (number_flowers * 2.80) * 0.15
    else:
        price_tulips = number_flowers * 2.80
elif type_flowers == 'Narcissus':
    if number_flowers < 120:
        price_narcissus = number_flowers * 3 + (number_flowers * 3) * 0.15
    else:
        price_narcissus = number_flowers * 3
elif type_flowers == 'Gladiolus':
    if number_flowers < 80:
        price_gladiolus = number_flowers * 2.50 + (number_flowers * 2.50) * 0.2
    else:
        price_gladiolus = number_flowers * 2.50

if type_flowers == 'Roses':
    if price_roses > budget:
        money_needed = price_roses - budget
        print(f'Not enough money, you need {money_needed:.2f} leva more.')
    elif price_roses <= budget:
        money_left = budget - price_roses
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.')
if type_flowers == 'Dahlias':
    if price_dahlias > budget:
        money_needed = price_dahlias - budget
        print(f'Not enough money, you need {money_needed:.2f} leva more.')
    elif price_dahlias <= budget:
        money_left = budget - price_dahlias
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.')
if type_flowers == 'Tulips':
    if price_tulips > budget:
            money_needed = price_tulips - budget
            print(f'Not enough money, you need {money_needed:.2f} leva more.')
    elif price_tulips <= budget:
            money_left = budget - price_tulips
            print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.')
if type_flowers == 'Narcissus':
    if price_narcissus > budget:
            money_needed = price_narcissus - budget
            print(f'Not enough money, you need {money_needed:.2f} leva more.')
    elif price_narcissus <= budget:
            money_left = budget - price_narcissus
            print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.')
if type_flowers == 'Gladiolus':
    if price_gladiolus > budget:
            money_needed = price_gladiolus - budget
            print(f'Not enough money, you need {money_needed:.2f} leva more.')
    elif price_gladiolus <= budget:
            money_left = budget - price_gladiolus
            print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.')
