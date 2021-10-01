a1 = int(input())
a2 = int(input())
n = int(input())

result = ''
command = n // 2

for symbol1 in range (a1, a2):
    for symbol2 in range (1, n):
        for symbol3 in range(1, command):

            symbol4 = symbol1
            if symbol1 % 2 == 1 and (symbol2 + symbol3 + symbol4) % 2 == 1:
                result += (chr(symbol1) + '-' + str(symbol2) + str(symbol3) + str(symbol1) + ' ')

print(result)




