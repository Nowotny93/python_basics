minutes_per_day = int(input())
number_walkings_per_day = int(input())
calories_per_day = int(input())

total_minutes_walking = minutes_per_day * number_walkings_per_day
total_burned_calories_per_day = total_minutes_walking * 5
half_calories = calories_per_day * 0.5

if total_burned_calories_per_day >= half_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories_per_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories_per_day}.')