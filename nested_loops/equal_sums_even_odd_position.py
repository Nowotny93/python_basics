# 1. отпечатваме всички в дадения диапазон
start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    # сума от цифрите на четни позиции == сума от цифрите на нечетни позиции
    # 376214
    units = number % 10  # even
    tens = number // 10 % 10  # odd
    hundreds = number // 100 % 10  # even
    thousands = number // 1000 % 10  # odd
    tens_thousands = number // 10000 % 10  # even
    hundred_thousands = number // 100000  # odd

    sum_even = units + hundreds + tens_thousands
    sum_odd = tens + thousands + hundred_thousands
    if sum_odd == sum_even:
        print(number, end=" ")