width = int(input())
lenght = int(input())

total_pieces = width * lenght
cake_enough = True
command = input()

while command != 'STOP':
    number_of_pieces = int(command)
    total_pieces -= number_of_pieces
    if total_pieces < 0 :
        cake_enough = False
        break
    command = input()

if cake_enough:
    print(f'{total_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')