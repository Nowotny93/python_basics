import math

figure = str(input())
side = float(input())

if figure == 'square':
    area_of_square = side * side
    print(round(area_of_square, 3))
elif figure == 'rectangle':
    side1 = float(input())
    area_of_rectangle = side * side1
    print(round(area_of_rectangle, 3))
elif figure == 'circle':
    area_of_circle = side * side * math.pi
    print(round(area_of_circle, 3))
elif figure == 'triangle':
    height = float(input())
    area_of_triangle = (side * height) / 2
    print(round(area_of_triangle, 3))

