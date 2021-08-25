product = str(input())
town = str(input())
quantity = float(input())

if product == "coffee":
    if town == 'Sofia':
        price = quantity * 0.50
        print(f'{price:.1f}')
    elif town == "Plovdiv":
        price = quantity * 0.40
        print(f'{price:.1f}')
    else:
        price = quantity * 0.45
        print(f'{price:.1f}')
elif product == "water":
    if town == 'Sofia':
        price = quantity * 0.80
        print(f'{price:.1f}')
    elif town == "Plovdiv":
        price = quantity * 0.70
        print(f'{price:.1f}')
    else:
        price = quantity * 0.70
        print(f'{price:.1f}')
elif product == "beer":
    if town == 'Sofia':
        price = quantity * 1.20
        print(f'{price:.1f}')
    elif town == "Plovdiv":
        price = quantity * 1.15
        print(f'{price:.2f}')
    else:
        price = quantity * 1.10
        print(f'{price:.1f}')
elif product == "sweets":
    if town == 'Sofia':
        price = quantity * 1.45
        print(price)
    elif town == "Plovdiv":
        price = quantity * 1.30
        print(f'{price:.1f}')
    else:
        price = quantity * 1.35
        print(f'{price:.5f}')
elif product == "peanuts":
    if town == 'Sofia':
        price = quantity * 1.60
        print(f'{price:.1f}')
    elif town == "Plovdiv":
        price = quantity * 1.50
        print(f'{price:.1f}')
    else:
        price = quantity * 1.55
        print(f'{price:.1f}')