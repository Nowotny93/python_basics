number_juniors = int(input())
number_seniors = int(input())
type_track = str(input())

if type_track == 'trail':
    price_juniors = number_juniors * 5.50
    price_seniors = number_seniors * 7
    total = price_seniors + price_juniors
elif type_track == 'cross-country':
    if (number_seniors + number_juniors) >= 50:
        price_juniors = number_juniors * 8 - (number_juniors * 8) * 0.25
        price_seniors = number_seniors * 9.50 - (number_seniors * 9.50) * 0.25
        total = price_seniors + price_juniors
    else:
        price_juniors = number_juniors * 8
        price_seniors = number_seniors * 9.50
        total = price_seniors + price_juniors
elif type_track == 'downhill':
    price_juniors = number_juniors * 12.25
    price_seniors = number_seniors * 13.75
    total = price_seniors + price_juniors
else:
    price_juniors = number_juniors * 20
    price_seniors = number_seniors * 21.50
    total = price_seniors + price_juniors

expenses = total * 0.05
total1 = total - expenses
print(f'{total1:.2f}')
