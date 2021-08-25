season = str(input())
type_group = str(input())
number_students = int(input())
number_nights = int(input())

price = 0
discount = 0

if type_group == 'boys' or type_group == 'girls':
    if season == 'Winter':
        price = number_nights * 9.60 * number_students
    elif season == 'Spring':
        price = number_nights * 7.20 * number_students
    elif season == 'Summer':
        price = number_nights * 15 * number_students
elif type_group == 'mixed':
    if season == 'Winter':
        price = number_nights * 10 * number_students
    elif season == 'Spring':
        price = number_nights * 9.50 * number_students
    elif season == 'Summer':
        price = number_nights * 20 * number_students

if number_students >= 50:
    discount = price * 0.5
elif number_students>= 20 and number_students < 50:
    discount = price * 0.15
elif number_students >= 10 and number_students < 20:
    discount = price * 0.05

total_pice = price - discount

if type_group == 'girls':
    if season == 'Winter':
        print(f'Gymnastics {total_pice:.2f} lv.')
    elif season == 'Spring':
        print(f'Athletics {total_pice:.2f} lv.')
    elif season == 'Summer':
        print(f'Volleyball {total_pice:.2f} lv.')
elif type_group == 'boys':
    if season == 'Winter':
        print(f'Judo {total_pice:.2f} lv.')
    elif season == 'Spring':
        print(f'Tennis {total_pice:.2f} lv.')
    elif season == 'Summer':
        print(f'Football {total_pice:.2f} lv.')
elif type_group == 'mixed':
    if season == 'Winter':
        print(f'Ski {total_pice:.2f} lv.')
    elif season == 'Spring':
        print(f'Cycling {total_pice:.2f} lv.')
    elif season == 'Summer':
        print(f'Swimming {total_pice:.2f} lv.')


