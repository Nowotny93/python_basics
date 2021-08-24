import math

days = int(input())
food_left = int(input())
food_per_day_for_dog = float(input())
food_per_day_for_cat = float(input())
food_per_day_for_turtle = float(input())

needed_food_for_dog = days * food_per_day_for_dog
needed_food_for_cat = days * food_per_day_for_cat
needed_food_for_turtle = days * food_per_day_for_turtle / 1000

total_food = needed_food_for_dog + needed_food_for_cat + needed_food_for_turtle

if total_food < food_left :
    food_left1 = math.floor(food_left - total_food)
    print(f'{food_left1} kilos of food left.')
elif total_food > food_left:
    needed_food = math.ceil(total_food - food_left)
    print(f'{needed_food} more kilos of food are needed.')