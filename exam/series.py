budget = float(input())
number_of_series = int(input())

total_price = 0

for i in range (1, number_of_series + 1):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        price_after_discount = series_price - 0.5 * series_price
        total_price += price_after_discount
    elif series_name == "Lucifer":
        price_after_discount = series_price - 0.4 * series_price
        total_price += price_after_discount
    elif series_name == "Protector":
        price_after_discount = series_price - 0.3 * series_price
        total_price += price_after_discount
    elif series_name == "TotalDrama":
        price_after_discount = series_price - 0.2 * series_price
        total_price += price_after_discount
    elif series_name == "Area":
        price_after_discount = series_price - 0.1 * series_price
        total_price += price_after_discount
    else:
        price_after_discount = series_price
        total_price += price_after_discount

if budget >= total_price:
    left_money = budget - total_price
    print(f'You bought all the series and left with {left_money:.2f} lv.')
else:
    needed_money = total_price - budget
    print(f'You need {needed_money:.2f} lv. more to buy the series!')