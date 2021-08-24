import math

hours = int(input())
days = int(input())
workers = int(input())

hours_for_work = 8*(days - days * 0.1)
overtime = workers * (2 * days)
total_hours = math.floor(hours_for_work + overtime)

if total_hours > hours:
    hours_left = total_hours - hours
    print(f'Yes!{hours_left} hours left.')
elif total_hours < hours:
    hours_needed = hours - total_hours
    print(f'Not enough time!{hours_needed} hours needed.')