beginning_num = int(input())
end_num = int(input())

check1 = False

for units in range(beginning_num, end_num + 1):
    for tens in range(beginning_num, end_num + 1):
        for hundreds in range(beginning_num, end_num + 1):
            for thousands in range(beginning_num, end_num + 1):

                if (units % 2 == 0 and thousands % 2 == 1) and (tens + hundreds) % 2 == 0 and units > thousands:
                    check1 = True
                if (units % 2 == 1 and thousands % 2 == 0) and (tens + hundreds) % 2 == 0 and units > thousands:
                    check1 = True

                if check1:
                    print(f"{units}{tens}{hundreds}{thousands}", end=" ")
                    check1 = False


