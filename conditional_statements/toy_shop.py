excursion_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

discount = 0
sum = number_of_puzzles * 2.60 + number_of_dolls *3 + number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks *2
total_toys = number_of_minions + number_of_bears + number_of_puzzles + number_of_trucks + number_of_dolls

if total_toys >= 50:
    discount = sum * 0.25
else:
    discount = 0

sum_end = sum - discount
rent = sum_end * 0.1
profit = sum_end - rent
money_left = abs(profit - excursion_price)

if profit > excursion_price:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')