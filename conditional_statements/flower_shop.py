import math

magnolii = int(input())
ziumbiuli = int(input())
roses = int(input())
cactuses = int(input())
price_of_gift = float(input())

sum = magnolii * 3.25 + ziumbiuli * 4 + roses * 3.50 + cactuses * 8
taxes = sum * 0.05
profit = sum - taxes

if price_of_gift > profit:
    money_needed = math.ceil(price_of_gift - profit)
    print(f'She will have to borrow {money_needed} leva.')
elif price_of_gift < profit :
    money_left = math.floor(profit - price_of_gift)
    print(f'She is left with {money_left} leva.')