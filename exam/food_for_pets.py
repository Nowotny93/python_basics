import math

days = int(input())
total_quantity_food = int(input())

eaten_food_by_dog = 0
eaten_food_by_cat = 0
biscuits = 0
counter = 0

for i in range (1, days + 1):
    food_for_dog = int(input())
    food_for_cat = int(input())
    counter += 1
    eaten_food_by_dog += food_for_dog
    eaten_food_by_cat += food_for_cat
    if counter % 3 == 0:
        biscuits += (food_for_dog + food_for_cat) * 0.1

total_eaten_food = eaten_food_by_dog + eaten_food_by_cat
percentage_total_eaten_food = (total_eaten_food / total_quantity_food) * 100
percentage_total_eaten_food_by_dog = (eaten_food_by_dog / total_eaten_food) * 100
percentage_total_eaten_food_by_cat = (eaten_food_by_cat / total_eaten_food) * 100

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{percentage_total_eaten_food:.2f}% of the food has been eaten.')
print(f'{percentage_total_eaten_food_by_dog:.2f}% eaten from the dog.')
print(f'{percentage_total_eaten_food_by_cat:.2f}% eaten from the cat.')
