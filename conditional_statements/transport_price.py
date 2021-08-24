kilometers = int(input())
day_night = str(input())

if kilometers < 20 and day_night == 'day':
    price_taxi_day = 0.70 + 0.79*kilometers
    print(f'{price_taxi_day:.2f}')
elif kilometers < 20 and day_night == 'night':
    price_taxi_night = 0.70 + 0.90*kilometers
    print(f'{price_taxi_night:.2f}')
elif kilometers >= 20 and kilometers < 100:
    price_bus = 0.09*kilometers
    print(f'{price_bus:.2f}')
else:
    price_train = 0.06*kilometers
    print(f'{price_train:.2f}')