num = float(input())
merna_edinica = str(input())
merna_edinica1 = str(input())

result = 0

m_to_mm = num * 1000
m_to_cm = num * 100
cm_to_m = num / 100
mm_to_m = num / 1000
mm_to_cm = num / 10
cm_to_mm = num * 10

if merna_edinica == 'mm' and merna_edinica1 == 'm':
    print("%.3f" % mm_to_m)
elif merna_edinica == 'mm' and merna_edinica1 == 'cm':
    print("%.3f" % mm_to_cm)
elif merna_edinica == 'cm' and merna_edinica1 == 'mm':
    print("%.3f" % cm_to_mm)
elif merna_edinica == 'cm' and merna_edinica1 == 'm':
    print("%.3f" % cm_to_m)
elif merna_edinica == 'm' and merna_edinica1 == 'cm':
    print("%.3f" % m_to_cm)
elif merna_edinica == 'm' and merna_edinica1 == 'mm':
    print("%.3f" % m_to_mm)
else:
    print(f'{m_to_mm}')

