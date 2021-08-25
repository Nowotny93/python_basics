days = int(input())
type_room = str(input())
positive_negative = str(input())

nights = days - 1

if type_room == 'apartment' and positive_negative == 'positive':
    if nights < 10:
        price = (25 - 25 * 0.3) * nights + 0.25 * ((25 - 25 * 0.3) * nights)
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = (25 - 25 * 0.35) * nights + 0.25 * ((25 - 25 * 0.35) * nights)
        print(f'{price:.2f}')
    elif nights > 15:
        price = (25 - 25 * 0.5) * nights + 0.25 * ((25 - 25 * 0.5) * nights)
        print(f'{price:.2f}')
elif type_room == 'apartment' and positive_negative == 'negative':
    if nights < 10:
        price = (25 - 25 * 0.3) * nights - 0.1 * ((25 - 25 * 0.3) * nights)
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = (25 - 25 * 0.35) * nights - 0.1 * ((25 - 25 * 0.35) * nights)
        print(f'{price:.2f}')
    elif nights > 15:
        price = (25 - 25 * 0.5) * nights - 0.1 * ((25 - 25 * 0.5) * nights)
        print(f'{price:.2f}')
elif type_room == 'room for one person' and positive_negative == 'positive':
        price = 18 * nights + 0.25 * (18 * nights)
        print(f'{price:.2f}')
elif type_room == 'room for one person' and positive_negative == 'negative':
        price = 18 * nights - 0.1 * (18 * nights)
        print(f'{price:.2f}')
elif type_room == 'president apartment' and positive_negative == 'positive':
    if nights < 10:
        price = (35 - 35 * 0.1) * nights + 0.25 * ((35 - 35 * 0.1) * nights)
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = (35 - 35 * 0.15) * nights + 0.25 * ((35 - 35 * 0.15) * nights)
        print(f'{price:.2f}')
    elif nights > 15:
        price = (35 - 35 * 0.2) * nights + 0.25 * ((35 - 35 * 0.2) * nights)
        print(f'{price:.2f}')
elif type_room == 'president apartment' and positive_negative == 'negative':
    if nights < 10:
        price = (35 - 35 * 0.1) * nights - 0.1 * ((35 - 35 * 0.1) * nights)
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = (35 - 35 * 0.15) * nights - 0.1 * ((35 - 35 * 0.15) * nights)
        print(f'{price:.2f}')
    elif nights > 15:
        price = (35 - 35 * 0.2) * nights - 0.1 * ((35 - 35 * 0.2) * nights)
        print(f'{price:.2f}')
