command = input()  # число или "stop"
# спираме да четем числа command == "stop"
# продължаваме да четем числа: command != "stop"

sum_prime = 0  # сума на простите числа
sum_non_prime = 0  # сума на съставните числа

while command != "stop":
    # число под формата на тескт '7' -> 7
    number = int(command)
    # проверка дали е отрицателно
    if number < 0:
        print('Number is negative.')
    else:
        # проверка дали е просто или не -> броя на делитетелите
        count = 0  # броя на делителите
        for n in range(1, number + 1):
            if number % n == 0:
                count += 1

        # знам броя на делителите
        if count == 2:
            sum_prime += number
        else:
            sum_non_prime += number

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")