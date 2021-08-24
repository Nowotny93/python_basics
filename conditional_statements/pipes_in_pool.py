pool_in_litres = int(input())
debit_pipe1_per_hour = int(input())
debit_pipe2_per_hour = int(input())
hours_absence = float(input())

water_pipe1 = debit_pipe1_per_hour * hours_absence
water_pipe2 = debit_pipe2_per_hour * hours_absence
overall_water = water_pipe1 + water_pipe2
percentage_pipe1 = (water_pipe1 / overall_water) * 100
percentage_pipe2 = (water_pipe2 / overall_water) * 100
percentage_pool = (overall_water / pool_in_litres) * 100

if overall_water < pool_in_litres :
    print(f'The pool is {percentage_pool:.2f}% full. Pipe 1: {percentage_pipe1:.2f}%. Pipe 2: {percentage_pipe2:.2f}%."')
elif overall_water > pool_in_litres :
    overflow_quantity = overall_water - pool_in_litres
    print(f'For {hours_absence} hours the pool overflows with {overflow_quantity:.2f} liters.')