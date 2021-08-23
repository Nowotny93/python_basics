total = int(input())

command = input()
gathered_money = 0
cash = 0
cash_persons = 0
by_card = 0
by_card_persons = 0

while command != "End":
    price_cash = int(command)
    if price_cash > 100:
        print('Error in transaction!')
    if price_cash <= 100:
        cash += price_cash
        cash_persons += 1
        gathered_money += price_cash
        print('Product sold!')
    price_card = int(input())
    if price_card < 10:
        print('Error in transaction!')
    if price_card >= 10:
        by_card += price_card
        by_card_persons += 1
        gathered_money += price_card
        print('Product sold!')
    if gathered_money >= total:
        average_cash = cash / cash_persons
        average_by_card = by_card / by_card_persons
        print(f'Average CS: {average_cash:.2f}')
        print(f'Average CC: {average_by_card:.2f}')
        break
    command = input()

else:
    print('Failed to collect required money for charity.')

