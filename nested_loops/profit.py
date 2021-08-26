coins_1lev = int(input())
coins_2lev = int(input())
coins_5lev = int(input())
sum = int(input())

lev1 = 1
lev2 = 2
lev5 = 5

for i in range (0, coins_1lev + 1):
    for z in range (0, coins_2lev + 1):
        for m in range (0, coins_5lev + 1):

            if (i * lev1 + z * lev2 + m * lev5) == sum:
                print(f'{i} * 1 lv. + {z} * 2 lv. + {m} * 5 lv. = {sum} lv.')