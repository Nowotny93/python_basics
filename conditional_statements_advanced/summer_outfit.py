degrees = int(input())
part_of_day_and_night = str(input())

if part_of_day_and_night == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif part_of_day_and_night == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
else:
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

