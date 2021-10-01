k = int(input())
l = int(input())
m = int(input())
n = int(input())

number_of_substitutions = 0
no_more_substitutions = False

for symbol1 in range (k, 9):
    for symbol2 in range (9 , l - 1, -1):
        for symbol3 in range (m, 9):
            for symbol4 in range (9 , n - 1, -1):

                check1 = symbol1 % 2 == 0
                check2 = symbol3 % 2 == 0
                check3 = symbol2 % 2 != 0
                check4 = symbol4 % 2 != 0

                if check1 and check2 and check3 and check4:
                    if symbol1 != symbol3 or symbol2 != symbol4:
                        print(f'{symbol1}{symbol2} - {symbol3}{symbol4}')
                        number_of_substitutions += 1
                    else:
                        print('Cannot change the same player.')
                if number_of_substitutions == 6:
                    no_more_substitutions = True
                    break
            if no_more_substitutions:
                break
        if no_more_substitutions:
            break
    if no_more_substitutions:
        break
