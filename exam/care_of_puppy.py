total_kg_food = int(input())

total_kg_food_into_grams = total_kg_food * 1000
total_eaten_food = 0
grams_eaten_food_per_time = input()

while grams_eaten_food_per_time != "Adopted":
    grams_eaten_food_per_time = int(grams_eaten_food_per_time)
    total_eaten_food += grams_eaten_food_per_time
    grams_eaten_food_per_time = input()

if total_eaten_food <= total_kg_food_into_grams:
    left_food = total_kg_food_into_grams - total_eaten_food
    print(f'Food is enough! Leftovers: {left_food} grams.')
else:
    needed_food = total_eaten_food - total_kg_food_into_grams
    print(f'Food is not enough. You need {needed_food} grams more.')
