number_of_players = int(input())

points = 0

numbers_between_0_and_9 = 0
numbers_between_10_and_19 = 0
numbers_between_20_and_29 = 0
numbers_between_30_and_39 = 0
numbers_between_40_and_50 = 0
invalid_numbers = 0

for i in range (1, number_of_players + 1):
    number = int(input())
    if number >= 0 and number <= 9:
        points += 0.2 * number
        numbers_between_0_and_9 += 1
    elif number >= 10 and number <= 19:
        points += 0.3 * number
        numbers_between_10_and_19 += 1
    elif number >= 20 and number <= 29:
        points += 0.4 * number
        numbers_between_20_and_29 += 1
    elif number >= 30 and number <= 39:
        points += 50
        numbers_between_30_and_39 += 1
    elif number >= 40 and number <= 50:
        points += 100
        numbers_between_40_and_50 += 1
    else:
        points = points / 2
        invalid_numbers += 1

percentage_numbers_between_0_and_9 = (numbers_between_0_and_9 / number_of_players) * 100
percentage_numbers_between_10_and_19 = (numbers_between_10_and_19 / number_of_players) * 100
percentage_numbers_between_20_and_29 = (numbers_between_20_and_29 / number_of_players) * 100
percentage_numbers_between_30_and_39 = (numbers_between_30_and_39 / number_of_players) * 100
percentage_numbers_between_40_and_50 = (numbers_between_40_and_50 / number_of_players) * 100
percentage_invalid_numbers = (invalid_numbers / number_of_players) * 100

print(f'{points:.2f}')
print(f'From 0 to 9: {percentage_numbers_between_0_and_9:.2f}%')
print(f'From 10 to 19: {percentage_numbers_between_10_and_19:.2f}%')
print(f'From 20 to 29: {percentage_numbers_between_20_and_29:.2f}%')
print(f'From 30 to 39: {percentage_numbers_between_30_and_39:.2f}%')
print(f'From 40 to 50: {percentage_numbers_between_40_and_50:.2f}%')
print(f'Invalid numbers: {percentage_invalid_numbers:.2f}%')