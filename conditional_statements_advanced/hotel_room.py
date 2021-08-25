month = str(input())
nights = int(input())

if month == 'May' or month == 'October':
    if 7 < nights <= 14:
        price_studio = 50 * nights - (50 * nights) * 0.05
        price_apartment = 65 * nights
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
    elif nights > 14:
        price_studio = 50 * nights - (50 * nights) * 0.3
        price_apartment = 65 * nights - (65 * nights) * 0.1
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
    else:
        price_studio = 50 * nights
        price_apartment = 65 * nights
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
elif month == 'June' or month == 'September':
    if nights > 14:
        price_studio = 75.20 * nights - (75.20 * nights) * 0.2
        price_apartment = 68.70 * nights - (68.70 * nights) * 0.1
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
    else:
        price_studio = 75.20 * nights
        price_apartment = 68.70 * nights
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
else:
    if nights > 14:
        price_studio = 76 * nights
        price_apartment = 77 * nights - (77 * nights) *0.1
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
    else:
        price_studio = 76 * nights
        price_apartment = 77 * nights
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')