n = int(input())

p1 = 0
p2 = 0
p3 = 0

percentage_p1 = 0
percentage_p2 = 0
percentage_p3 = 0

for i in range (0, n):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

percentage_p1 = (p1 / n) * 100
percentage_p2 = (p2 / n) * 100
percentage_p3 = (p3 / n) * 100

print(f'{percentage_p1:.2f}%')
print(f'{percentage_p2:.2f}%')
print(f'{percentage_p3:.2f}%')
