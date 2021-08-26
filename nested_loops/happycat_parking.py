days = int(input())
hours = int(input())

tax_total_z = 0
tax_total = 0

for i in range (1, days + 1):
    for z in range (1, hours + 1):

        if i % 2 != 0 and z % 2 == 0:
            tax_total_z += 1.25
            tax_total += 1.25
        elif i % 2 == 0 and z % 2 != 0:
            tax_total_z += 2.50
            tax_total += 2.50
        else:
            tax_total_z += 1
            tax_total += 1
        if z == hours:
            print(f'Day: {i} - {tax_total_z:.2f} leva')
            tax_total_z = 0

print(f'Total: {tax_total:.2f} leva')


