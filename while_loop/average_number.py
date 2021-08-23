n = int(input())
sum = 0

for i in range (1, n+1):
    num = int(input())
    sum += num

average = sum / n
print (f'{average:.2f}')
