import sys

inpt = input()

min_number = sys.maxsize

while inpt != 'Stop':
    num = int(inpt)
    if num < min_number:
        min_number = num
    inpt = input()

print(min_number)