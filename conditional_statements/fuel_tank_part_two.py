type_fuel = str(input())
litres_fuel = float(input())
club_card = str(input())

if club_card == 'Yes':
    gas_per_liter = 0.85
    price_gas = litres_fuel * gas_per_liter
    gasoline_per_liter = 2.04
    price_gasoline = litres_fuel * gasoline_per_liter
    diesel_per_liter = 2.21
    price_diesel = litres_fuel * diesel_per_liter
elif club_card == 'No':
    gas_per_liter = 0.93
    price_gas = litres_fuel * gas_per_liter
    gasoline_per_liter = 2.22
    price_gasoline = litres_fuel * gasoline_per_liter
    diesel_per_liter = 2.33
    price_diesel = litres_fuel * diesel_per_liter

if type_fuel == 'Gas' and litres_fuel >= 20 and litres_fuel <= 25:
        total_price_gas = price_gas - price_gas * 0.08
        print(f'{total_price_gas:.2f} lv.')
elif type_fuel == 'Gasoline' and litres_fuel >= 20 and litres_fuel <= 25:
        total_price_gasoline = price_gasoline - price_gasoline * 0.08
        print(f'{total_price_gasoline:.2f} lv.')
elif type_fuel == 'Diesel' and litres_fuel >= 20 and litres_fuel <= 25:
        total_price_diesel = price_diesel - price_diesel * 0.08
        print(f'{total_price_diesel:.2f} lv.')
elif type_fuel == 'Gas' and litres_fuel > 25:
    total_price_gas = price_gas - price_gas * 0.1
    print(f'{total_price_gas:.2f} lv.')
elif type_fuel == 'Gasoline' and litres_fuel > 25:
    total_price_gasoline = price_gasoline - price_gasoline * 0.1
    print(f'{total_price_gasoline:.2f} lv.')
elif type_fuel == 'Diesel' and litres_fuel > 25:
    total_price_diesel = price_diesel - price_diesel * 0.1
    print(f'{total_price_diesel:.2f} lv.')
elif type_fuel == 'Gas' and litres_fuel < 20:
    print(f'{price_gas:.2f} lv.')
elif type_fuel == 'Gasoline' and litres_fuel < 20:
    print(f'{price_gasoline:.2f} lv.')
elif type_fuel == 'Diesel' and litres_fuel < 20:
    print(f'{price_diesel:.2f} lv.')
