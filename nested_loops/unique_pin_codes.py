limit_first_number = int(input())
limit_second_number = int(input())
limit_third_number = int(input())

for num1 in range (1, limit_first_number + 1):
    for num2 in range(1, limit_second_number + 1):
        for num3 in range(1, limit_third_number + 1):

                check1 = num1 % 2 == 0
                check2 = num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7
                check3 = num3 % 2 == 0

                if check1 and check2 and check3:
                    print(f'{num1} {num2} {num3}')


