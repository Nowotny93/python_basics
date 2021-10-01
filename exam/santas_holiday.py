days = int(input())
type_room = input()
comment = input()

nights = days - 1
price = 0

if days < 10:
    if type_room == "room for one person":
        price = nights * 18
    elif type_room == "apartment":
        price = nights * 25 - 0.3 * (nights * 25)
    elif type_room == "president apartment":
        price = nights * 35 - 0.1 * (nights * 35)
elif 10 <= days <= 15:
    if type_room == "room for one person":
        price = nights * 18
    elif type_room == "apartment":
        price = nights * 25 - 0.35 * (nights * 25)
    elif type_room == "president apartment":
        price = nights * 35 - 0.15 * (nights * 35)
else:
    if type_room == "room for one person":
        price = nights * 18
    elif type_room == "apartment":
        price = nights * 25 - 0.5 * (nights * 25)
    elif type_room == "president apartment":
        price = nights * 35 - 0.2 * (nights * 35)

if comment == "positive":
    price_after_comment = price + price * 0.25
    print(f'{price_after_comment:.2f}')
else:
    price_after_comment = price - price * 0.1
    print(f'{price_after_comment:.2f}')

