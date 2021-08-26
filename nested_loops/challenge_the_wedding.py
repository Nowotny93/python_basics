number_men = int(input())
number_women = int(input())
max_number_tables = int(input())

counter = 0

for i in range (1, number_men + 1):
    for z in range (1, number_women + 1):

        counter += 1
        if counter > max_number_tables:
            break
        print(f'({i} <-> {z}) ', end = "")

