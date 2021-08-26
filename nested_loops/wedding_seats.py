last_sector = input()
rows_first_sector = int(input())
seats_odd = int(input())

seats_even = seats_odd + 2
result = ''

for i in range (ord('a'), ord(last_sector) + 1):
    for z in range (1, rows_first_sector + 1):
        for m in range (ord('a'), ord('z')):

            if m % 2 == 1:
                m = seats_odd
                result += ('' + chr(i) + str(z) + chr(m) + ' ')
            else:
                m = seats_even
                result += ('' + chr(i) + str(z) + chr(m) + ' ')









