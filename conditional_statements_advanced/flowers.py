number_hrizantemas = int(input())
number_roses = int(input())
number_tulips = int(input())
season = str(input())
is_holiday = str(input())

discount1 = 0
discount2 = 0
discount3 = 0
price_flowers = 0

if season == 'Spring' or season == 'Summer':
    price_hrizantemas = 2 * number_hrizantemas
    price_roses = 4.10 * number_roses
    price_tulips = 2.50 * number_tulips
elif season == 'Autumn' or season == 'Winter':
    price_hrizantemas = 3.75 * number_hrizantemas
    price_roses = 4.50 * number_roses
    price_tulips = 4.15 * number_tulips

if is_holiday == 'Y':
    price_hrizantemas = price_hrizantemas + price_hrizantemas * 0.15
    price_roses = price_roses + price_roses * 0.15
    price_tulips = price_tulips + price_tulips * 0.15
    price_flowers = price_roses + price_hrizantemas + price_tulips
else:
    price_flowers = price_roses + price_hrizantemas + price_tulips

if number_tulips > 7 and season == 'Spring':
        discount1 = price_flowers * 0.05
if number_roses >= 10 and season == 'Winter':
        discount2 = price_flowers * 0.1
if (number_roses + number_tulips + number_tulips) > 20:
        discount3 = price_flowers * 0.2


price_flowers_after_package = price_flowers - discount1 - discount2 - discount3 + 2
print (f'{price_flowers_after_package:.2f}')