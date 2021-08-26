n = int(input())
l = int(input())

result = ''
for symbol1 in range (1, n+1):
    for symbol2 in range (1, n+1):
        for symbol3 in range(ord('a'), l+ord('a')):
            for symbol4 in range(ord('a'), l+ord('a')):
                for symbol5 in range(max(symbol1, symbol2) + 1, n + 1):
                    result += ('' + str(symbol1) + str(symbol2) + chr(symbol3) + chr(symbol4) + str(symbol5) + ' ')

print(result.strip())



