symbol = input()

counter_spec = 0
script = ''
word = 0
counter = 1


while symbol != "End":
    next_symbol = str(symbol)
    if next_symbol == 'n' or next_symbol == 'o' or next_symbol == 'c':
        counter_spec += 1
        if counter_spec % 2 == 0:
            script += next_symbol
            counter_spec = 0
        if counter % 3 == 0:
            print(f'{script} ')
        counter += 1
        symbol = input()
        continue

    script += next_symbol
    symbol = input()
