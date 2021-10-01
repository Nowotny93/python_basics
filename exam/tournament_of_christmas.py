days = int(input())

sport = input()
gathered_money = 0
win_money = 0
won_games = 0
lost_games = 0
total_won_games = 0
total_lost_games = 0

for i in range(1, days + 1):
    while sport != "Finish":
        result = input()
        if result == "win":
            gathered_money += 20
            win_money += 20
            won_games += 1
            total_won_games +=1
        elif result == "lose":
            lost_games += 1
            total_lost_games +=1
        sport = input()
    if won_games > lost_games:
        gathered_money += win_money * 0.1
        win_money = 0

    if i == days:
        break
    win_money = 0
    won_games = 0
    lost_games = 0
    sport = input()

if total_won_games > total_lost_games:
    gathered_money += gathered_money * 0.2
    print(f"You won the tournament! Total raised money: {gathered_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {gathered_money:.2f}")

