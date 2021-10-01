movie = input()

result = 0
counter = 0
max_sum = -1
best_movie = ''

while movie != "STOP":
    result = 0
    counter += 1
    for i in movie:
        result += ord(i)
        if i >= "A" and i <= "Z":
            result -= len(movie)
        if i >= "a" and i <= "z":
            result -= len(movie) * 2
    if result > max_sum:
        max_sum = result
        best_movie = movie
    if counter == 7:
        print('The limit is reached.')
        print(f'The best movie for you is {best_movie} with {max_sum} ASCII sum.')
        break
    movie = input()

else:
    print(f'The best movie for you is {best_movie} with {max_sum} ASCII sum.')