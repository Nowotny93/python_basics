first_letter = input()
second_letter = input()
exclude_letter = input()

exclusion = False
combinations = 0
result = ''

for i in range (ord(first_letter), ord(second_letter) + 1):
    for z in range (ord(first_letter), ord(second_letter) + 1):
        for m in range (ord(first_letter), ord(second_letter) + 1):

            if m == ord(exclude_letter) or z == ord(exclude_letter) or i == ord(exclude_letter):
                exclusion = True
            if exclusion:
                exclusion = False
                continue

            combinations += 1
            result +=  ('' + chr(i) + chr(z) + chr(m) + ' ')

print(f'{result}{combinations}')