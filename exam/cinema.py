capacity = int(input())
command = input()

booked_seats = 0
total_income = 0
is_full = False


while command != "Movie time!":
    number_of_people = int(command)
    booked_seats += number_of_people
    if booked_seats > capacity:
        is_full = True
        break
    if number_of_people % 3 == 0:
        total_income += (number_of_people * 5) - 5
    else:
        total_income += number_of_people * 5
    command = input()

if is_full:
    print(f'The cinema is full.')
    print(f'Cinema income - {total_income} lv.')
else:
    seats_left = capacity - booked_seats
    print(f'There are {seats_left} seats left in the cinema.')
    print(f'Cinema income - {total_income} lv.')


