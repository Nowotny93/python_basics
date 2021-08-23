needed_money = float(input())
present_money = float(input())

days = 0
days_to_stop = 0

while present_money < needed_money:
    operation = input()
    days += 1
    amount = float(input())
    if operation == 'spend':
        days_to_stop += 1
        present_money -= amount
        if present_money < 0:
            present_money = 0
    elif operation == 'save':
        days_to_stop = 0
        present_money += amount

    if days_to_stop == 5:
        print(f"You can't save the money.")
        print(days)
        break
else:
    print(f'You saved the money for {days} days.')
