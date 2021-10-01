goal = int(input())

command = input()
saved_money = 0

while command != "closed":
    if command == "haircut":
        type_haircut = input()
        if type_haircut == "mens":
            saved_money += 15
        elif type_haircut == "ladies":
            saved_money += 20
        elif type_haircut == "kids":
            saved_money += 10
    elif command == "color":
        type_color = input()
        if type_color == "touch up":
            saved_money += 20
        elif type_color == "full color":
            saved_money += 30
    if saved_money >= goal:
        break
    command = input()

if saved_money >= goal:
    print('You have reached your target for the day!')
    print(f'Earned money: {saved_money}lv.')
else:
    needed_money = goal - saved_money
    print(f'Target not reached! You need {needed_money}lv. more.')
    print(f'Earned money: {saved_money}lv.')