n = int(input())
name_of_presentation = input()

sum_grades = 0
sum_individual = 0
counter = 0

while name_of_presentation != "Finish":
    for i in range(1, n+1):
        grade = float(input())
        sum_grades += grade
        sum_individual += grade
        counter += 1
    average_grade = sum_individual / n
    print(f'{name_of_presentation} - {average_grade:.2f}.')
    sum_individual = 0
    name_of_presentation = input()

average_total = sum_grades / counter
print(f"Student's final assessment is {average_total:.2f}.")

