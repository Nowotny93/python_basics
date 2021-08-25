import sys

max_num = sys.maxsize

for i in range(1, max_num):
    num = float(input())
    if num >= 0:
        num_multiplied = num * 2
        print(f'Result: {num_multiplied:.2f}')
    else:
        break

print('Negative number!')
