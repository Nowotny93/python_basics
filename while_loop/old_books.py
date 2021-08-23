name_of_book = str(input())

sum_of_books = 0
random_book = input()
right_book = True

while random_book != name_of_book:
    if random_book == 'No More Books':
        right_book = False
        break
    sum_of_books += 1
    random_book = input()

if right_book:
    print(f'You checked {sum_of_books} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {sum_of_books} books.')

