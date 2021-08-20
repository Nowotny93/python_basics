stadium_capacity = int(input())
count_fans = int(input())

fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for i in range (1, count_fans + 1):
    sector = str(input())
    if sector == 'A':
        fans_a += 1
    if sector == 'B':
        fans_b += 1
    if sector == 'V':
        fans_v += 1
    if sector == 'G':
        fans_g += 1

percentage_fans_a = (fans_a / count_fans) * 100
percentage_fans_b = (fans_b / count_fans) * 100
percentage_fans_v = (fans_v / count_fans) * 100
percentage_fans_g = (fans_g / count_fans) * 100
percentage_all_fans = (count_fans / stadium_capacity) * 100

print(f'{percentage_fans_a:.2f}%')
print(f'{percentage_fans_b:.2f}%')
print(f'{percentage_fans_v:.2f}%')
print(f'{percentage_fans_g:.2f}%')
print(f'{percentage_all_fans:.2f}%')