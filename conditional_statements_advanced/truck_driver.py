season = str(input())
kilometers_per_month = float(input())

if kilometers_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price = (kilometers_per_month * 0.75) * 4
    elif season == 'Summer':
        price = (kilometers_per_month * 0.9) * 4
    else:
        price = (kilometers_per_month * 1.05) * 4
elif 5000 < kilometers_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price = (kilometers_per_month * 0.95) * 4
    elif season == 'Summer':
        price = (kilometers_per_month * 1.10) * 4
    else:
        price = (kilometers_per_month * 1.25) * 4
elif 10000 < kilometers_per_month <= 20000:
    price = (kilometers_per_month * 1.45) * 4

total_salary = price - price * 0.1
print(f'{total_salary:.2f}')
