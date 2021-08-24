import math

total_area_grapes = int(input())
grapes_per_meter = float(input())
litres_wine_needed = int(input())
number_of_workers = int(input())

grapes_total = total_area_grapes * grapes_per_meter
wine = (0.4 * grapes_total) / 2.5

if wine > litres_wine_needed:
    litres_left = math.ceil(wine - litres_wine_needed)
    litres_per_person = math.ceil(litres_left / number_of_workers)
    print(f'Good harvest this year! Total wine: {wine:.0f} liters.')
    print(f'{litres_left} liters left -> {litres_per_person} liters per person.')
elif wine < litres_wine_needed:
    litres_left = math.floor(litres_wine_needed - wine)
    print(f'It will be a tough winter! More {litres_left} liters wine needed.')


