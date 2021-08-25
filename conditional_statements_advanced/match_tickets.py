budget = float(input())
category = str(input())
people = int(input())

if 1 <= people <= 4:
    transport = budget * 0.75
    budget_end = budget - transport
elif 5 <= people <= 9:
    transport = budget * 0.6
    budget_end = budget - transport
elif 10 <= people <= 24:
    transport = budget * 0.5
    budget_end = budget - transport
elif 25 <= people <= 49:
    transport = budget * 0.4
    budget_end = budget - transport
else:
    transport = budget * 0.25
    budget_end = budget - transport

if category == "Normal":
    money_for_ticket = people * 249.99
else:
    money_for_ticket = people * 499.99

if money_for_ticket <= budget_end:
    money_left = budget_end - money_for_ticket
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = money_for_ticket - budget_end
    print(f'Not enough money! You need {money_needed:.2f} leva.')
