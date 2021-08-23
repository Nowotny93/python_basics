money = input()
sum = 0

while money != 'NoMoreMoney':
    amount = float(money)
    if amount < 0:
        print('Invalid operation!')
        break
    sum += amount
    print(f'Increase: {amount:.2f}')
    money = input()

print(f'Total: {sum:.2f}')
