pocket_money_per_day = float(input())
earned_money_per_day = float(input())
total_costs = float(input())
price_of_gift = float(input())

saved_money_from_pocket_money = 5 * pocket_money_per_day
saved_money_from_sales = 5 * earned_money_per_day
total_saved_money = saved_money_from_pocket_money + saved_money_from_sales
total_saved_money_after_costs = total_saved_money - total_costs

if total_saved_money_after_costs >= price_of_gift:
    print(f'Profit: {total_saved_money_after_costs:.2f} BGN, the gift has been purchased.')
else:
    needed_money = price_of_gift - total_saved_money_after_costs
    print(f'Insufficient money: {needed_money:.2f} BGN.')