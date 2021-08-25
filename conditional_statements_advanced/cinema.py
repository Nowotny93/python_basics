type = str(input())
rows = int(input())
columns = int(input())

if type == 'Premiere':
    price = rows * columns * 12
    print(f'{price:.2f} leva')
elif type == 'Normal':
    price = rows * columns * 7.50
    print(f'{price:.2f} leva')
else:
    price = rows * columns * 5.00
    print(f'{price:.2f} leva')