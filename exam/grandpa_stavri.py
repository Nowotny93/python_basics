days = int(input())

total_quantity = 0
total_degrees = 0

for i in range (1, days + 1):
    quantity = float(input())
    degrees = float(input())
    total_quantity += quantity
    total_degrees += quantity * degrees

average_degrees = total_degrees / total_quantity

print(f'Liter: {total_quantity:.2f}')
print(f'Degrees: {average_degrees:.2f}')
if average_degrees < 38:
    print('Not good, you should baking!')
elif 38 <= average_degrees <= 42:
    print('Super!')
else:
    print(f'Dilution with distilled water!')