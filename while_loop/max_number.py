import sys

inpt = input()

max_number = -sys.maxsize

while inpt != 'Stop':
    num = int(inpt)
    if num > max_number:
        max_number = num
    inpt = input()

print(max_number)