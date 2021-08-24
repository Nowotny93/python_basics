holiday = int(input())

working_days = 365-holiday
gaming_time = working_days * 63 + holiday * 127
norm_difference = abs(30000 - gaming_time)
hours = norm_difference // 60
minutes = norm_difference % 60

if gaming_time > 30000:
    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
elif gaming_time < 30000:
    print("Tom sleeps well")
    print(f'{hours} hours and {minutes} minutes less for play')
