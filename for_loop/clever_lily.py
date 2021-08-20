ages = int(input())
laundry_price = float(input())
toy_price = int(input())

birthday_money = 0
total_money = 0
total_toys = 0

for birthday in range(1, ages + 1):
    if birthday % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1
    else:
        total_toys += 1
money_from_toys = total_toys * toy_price
total_money += money_from_toys
difference = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
