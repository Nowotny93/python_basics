months = int(input())

electricity = 0
electricity_sum = 0
water = 0
internet = 0
others = 0

for i in range (1, months + 1):
    electricity = float(input())
    electricity_sum += electricity
    water += 20
    internet += 15
    others += electricity + 20 + 15 + 0.2 * (electricity + 20 + 15)

average = (electricity_sum + water + internet + others) / months

print(f'Electricity: {electricity_sum:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')
