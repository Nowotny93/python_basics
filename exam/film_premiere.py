movie = input()
movie_package = input()
tickets = int(input())

if movie == "John Wick":
    if movie_package == "Drink":
        price = 12 * tickets
    elif movie_package == "Popcorn":
        price = 15 * tickets
    elif movie_package == "Menu":
        price = 19 * tickets
elif movie == "Star Wars":
    if tickets >= 4:
        if movie_package == "Drink":
            price = 18 * tickets - (0.3 * (18 * tickets))
        elif movie_package == "Popcorn":
            price = 25 * tickets - (0.3 * (25 * tickets))
        elif movie_package == "Menu":
            price = 30 * tickets - (0.3 * (30 * tickets))
    else:
        if movie_package == "Drink":
            price = 18 * tickets
        elif movie_package == "Popcorn":
            price = 25 * tickets
        elif movie_package == "Menu":
            price = 30 * tickets
elif movie == "Jumanji":
    if tickets == 2:
        if movie_package == "Drink":
            price = 9 * tickets - (0.15 * (9 * tickets))
        elif movie_package == "Popcorn":
            price = 11 * tickets - (0.15 * (11 * tickets))
        elif movie_package == "Menu":
            price = 14 * tickets - (0.15 * (14 * tickets))
    else:
        if movie_package == "Drink":
            price = 9 * tickets
        elif movie_package == "Popcorn":
            price = 11 * tickets
        elif movie_package == "Menu":
            price = 14 * tickets

print(f'Your bill is {price:.2f} leva.')
