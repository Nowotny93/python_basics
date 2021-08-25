fruit = str(input())
day = str(input())
quantity = float(input())

if fruit == 'banana':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_banana = 2.50 * quantity
        print(f'{price_banana:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_banana1 = 2.70 * quantity
        print(f'{price_banana1:.2f}')
    else:
        print('error')
elif fruit == 'apple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_apple = 1.20 * quantity
        print(f'{price_apple:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_apple1 = 1.25 * quantity
        print(f'{price_apple1:.2f}')
    else:
        print('error')
elif fruit == 'orange':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_orange = 0.85 * quantity
        print(f'{price_orange:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_orange1 = 0.90 * quantity
        print(f'{price_orange1:.2f}')
    else:
        print('error')
elif fruit == 'grapefruit':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_grapefruit = 1.45 * quantity
        print(f'{price_grapefruit:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_grapefruit1 = 1.60 * quantity
        print(f'{price_grapefruit1:.2f}')
    else:
        print('error')
elif fruit == 'kiwi':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_kiwi = 2.70 * quantity
        print(f'{price_kiwi:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_kiwi1 = 3.00 * quantity
        print(f'{price_kiwi1:.2f}')
    else:
        print('error')
elif fruit == 'grapes':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_grapes = 3.85 * quantity
        print(f'{price_grapes:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_grapes1 = 4.20 * quantity
        print(f'{price_grapes1:.2f}')
    else:
        print('error')
elif fruit == 'pineapple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price_pineapple = 5.50 * quantity
        print(f'{price_pineapple:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        price_pineapple1 = 5.60 * quantity
        print(f'{price_pineapple1:.2f}')
    else:
        print('error')
else:
    print('error')





