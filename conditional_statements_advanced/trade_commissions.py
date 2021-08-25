town = str(input())
sells = float(input())

if 0 <= sells <= 500:
    if town == 'Sofia':
        commission = sells * 0.05
        print(f'{commission:.2f}')
    elif town == 'Varna':
        commission = sells * 0.045
        print(f'{commission:.2f}')
    elif town == 'Plovdiv':
        commission = sells * 0.055
        print(f'{commission:.2f}')
    else:
        print('error')
elif 500 <= sells <= 1000:
    if town == 'Sofia':
        commission = sells * 0.07
        print(f'{commission:.2f}')
    elif town == 'Varna':
        commission = sells * 0.075
        print(f'{commission:.2f}')
    elif town == 'Plovdiv':
        commission = sells * 0.08
        print(f'{commission:.2f}')
    else:
        print('error')
elif 1000 <= sells <= 10000:
    if town == 'Sofia':
        commission = sells * 0.08
        print(f'{commission:.2f}')
    elif town == 'Varna':
        commission = sells * 0.1
        print(f'{commission:.2f}')
    elif town == 'Plovdiv':
        commission = sells * 0.12
        print(f'{commission:.2f}')
    else:
        print('error')
elif sells > 10000:
    if town == 'Sofia':
        commission = sells * 0.12
        print(f'{commission:.2f}')
    elif town == 'Varna':
        commission = sells * 0.13
        print(f'{commission:.2f}')
    elif town == 'Plovdiv':
        commission = sells * 0.145
        print(f'{commission:.2f}')
    else:
        print('error')
else:
    print('error')