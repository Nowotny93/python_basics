budget = float(input())
season = str(input())

if budget <= 100:
    if season == "summer":
        place = 'Somewhere in Bulgaria'
        type = 'Camp'
        price = budget * 0.3
        print(place)
        print(f'{type} - {price:.2f}')
    elif season == "winter":
        place = 'Somewhere in Bulgaria'
        type = 'Hotel'
        price = budget * 0.7
        print(place)
        print(f'{type} - {price:.2f}')
elif 100 < budget <= 1000:
    if season == "summer":
        place = 'Somewhere in Balkans'
        type = 'Camp'
        price = budget * 0.4
        print(place)
        print(f'{type} - {price:.2f}')
    elif season == "winter":
        place = 'Somewhere in Balkans'
        type = 'Hotel'
        price = budget * 0.8
        print(place)
        print(f'{type} - {price:.2f}')
else:
    place = 'Somewhere in Europe'
    type = 'Hotel'
    price = budget * 0.9
    print(place)
    print(f'{type} - {price:.2f}')

