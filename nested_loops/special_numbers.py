n = int(input())
# 1111 до 9999
for number in range(1111, 10000):
    # print only special
    # вземем всяка една цифра
    # 3456 -> 3    4    5   6
    units = number % 10  # единици
    tens = number // 10 % 10  # десетици
    hundreds = number // 100 % 10  # стотици
    thousands = number // 1000  # хилядни

    check1 = units != 0 and n % units == 0
    check2 = tens != 0 and n % tens == 0
    check3 = hundreds != 0 and n % hundreds == 0
    check4 = n % thousands == 0

    if check1 and check2 and check3 and check4:
        print(number, end=' ')

