loads = int(input())

price_microbus = 0
price_truck = 0
price_train = 0
total_price = 0

tons_microbus = 0
tons_truck = 0
tons_train = 0
load_in_tons = 0

for i in range (1, loads+1):
    load = int(input())
    if load <= 3:
        price_microbus = 200 * load
        total_price += price_microbus
        load_in_tons += load
        tons_microbus += load
    elif load >= 4 and load <= 11:
        price_truck = 175 * load
        total_price += price_truck
        load_in_tons += load
        tons_truck += load
    elif load >= 12:
        price_train = 120 * load
        total_price += price_train
        load_in_tons += load
        tons_train += load

average_price = total_price / load_in_tons
percentage_tons_microbus = (tons_microbus / load_in_tons) * 100
percentage_tons_truck = (tons_truck / load_in_tons) * 100
percentage_tons_train = (tons_train / load_in_tons) * 100

print(f'{average_price:.2f}')
print(f'{percentage_tons_microbus:.2f}%')
print(f'{percentage_tons_truck:.2f}%')
print(f'{percentage_tons_train:.2f}%')