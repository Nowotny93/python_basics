type_fuel = str(input())
litres_fuel = float(input())

if type_fuel != 'Diesel' and type_fuel != 'Gasoline' and type_fuel != 'Gas':
    print('Invalid fuel!')
elif litres_fuel >= 25:
    print(f'You have enough {type_fuel}.')
elif litres_fuel < 25:
    print(f'Fill your tank with {type_fuel}!')
