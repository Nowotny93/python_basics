count_bottles = int(input())

quantity_total = count_bottles * 750
days_to_bigger_coups = 0
total_cleaned = 0
total_bigger_coups = 0
command = input()

while command != 'End' or quantity_total < 0:
    dirty_dishes = int(command)
    days_to_bigger_coups += 1
    total_cleaned += dirty_dishes
    if days_to_bigger_coups % 3 == 0:
        number_bigger_coups = dirty_dishes * 15
        quantity_total -= number_bigger_coups
        total_bigger_coups += dirty_dishes
        if quantity_total < 0:
            print(f'Not enough detergent, {abs(quantity_total)} ml. more necessary!')
            break
        command = input()
        continue
    number_plates = dirty_dishes * 5
    quantity_total -= number_plates
    if quantity_total < 0:
        print(f'Not enough detergent, {abs(quantity_total)} ml. more necessary!')
        break
    command = input()

else:
    total_plates = total_cleaned - total_bigger_coups
    print('Detergent was enough!')
    print(f'{total_plates} dishes and {total_bigger_coups} pots were washed.')
    print(f'Leftover detergent {quantity_total} ml.')
