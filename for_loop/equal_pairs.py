n = int(input())

number1 = 0

for i in range(0, n):
    num1 = int(input())
    num2 = int(input())
    number1 += num1 + num2

if number1 % n == 0:
    total = number1 / n
    print(f'Yes, value={total:.0f}')
else:
    total1 = number1 // n
    print(f'No, maxdiff={total1:.0f}')
