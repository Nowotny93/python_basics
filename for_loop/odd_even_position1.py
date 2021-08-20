import sys
smallest_even = sys.maxsize
biggest_even = -sys.maxsize
smallest_odd = sys.maxsize
biggest_odd = -sys.maxsize

count_of_numbers = int(input())
odd_sum = 0
even_sum = 0
for number in range (1, count_of_numbers + 1):
    current_number = float(input())
    if number % 2 == 0:
        even_sum += current_number
        if current_number < smallest_even :
            smallest_even = current_number
        if current_number > biggest_even:
            biggest_even = current_number
    else:
        odd_sum += current_number
        if current_number < smallest_odd :
            smallest_odd = current_number
        if current_number > biggest_odd:
            biggest_odd = current_number

print(f'OddSum={odd_sum:.2f},')

if smallest_odd == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={smallest_odd:.2f},')

if biggest_odd == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={biggest_odd:.2f},')

print(f'EvenSum={even_sum:.2f},')

if smallest_even == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={smallest_even:.2f},')

if biggest_even == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={biggest_even:.2f}')
