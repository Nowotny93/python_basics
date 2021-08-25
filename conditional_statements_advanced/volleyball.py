import math

type_year = str(input())
p = int(input())
h = int(input())

if type_year == 'leap':
    weekends_at_hometown = 48 - h
    saturday_games = weekends_at_hometown * 3 / 4
    holiday_games = p * (2 / 3)
    total_games = saturday_games + h + holiday_games
    additional_games = total_games + total_games * 0.15
    print(math.floor(additional_games))
else:
    weekends_at_hometown = 48 - h
    saturday_games = weekends_at_hometown * 3 / 4
    holiday_games = p * (2 / 3)
    total_games = saturday_games + h + holiday_games
    print(math.floor(total_games))
