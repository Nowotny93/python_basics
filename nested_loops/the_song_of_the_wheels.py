control_value = int(input())

fourth_number = ''
counter = 0
successfull_fourth_number = False

for a in range (1, 10):
    for b in range (1, 10):
        for c in range (1, 10):
            for d in range (1, 10):

                if a < b and c > d and ((a * b) + (c * d)) == control_value:
                    print(f'{a}{b}{c}{d}', end = " ")
                    counter += 1
                if a < b and c > d and ((a * b) + (c * d)) == control_value and counter == 4:
                    fourth_number += str(a) + str(b) + str(c) + str(d)
                    successfull_fourth_number = True

print()
if successfull_fourth_number:
    print(f'Password: {fourth_number}')
else:
    print('No!')
