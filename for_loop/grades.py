students = int(input())

students_between_2_and_3 = 0
students_between_3_and_4 = 0
students_between_4_and_5 = 0
students_above_5 = 0

grades_sum = 0

for i in range (1, students + 1):
    grade = float(input())
    if grade >= 2 and grade < 3:
        students_between_2_and_3 += 1
        grades_sum += grade
    elif grade >=3 and grade < 4:
        students_between_3_and_4 += 1
        grades_sum += grade
    elif grade >= 4 and grade < 5:
        students_between_4_and_5 += 1
        grades_sum += grade
    else:
        students_above_5 += 1
        grades_sum += grade

percentage_students_between_2_and_3 = (students_between_2_and_3 / students) * 100
percentage_students_between_3_and_4 = (students_between_3_and_4 / students) * 100
percentage_students_between_4_and_5 = (students_between_4_and_5 / students) * 100
percentage_students_above_5 = (students_above_5 / students) * 100
average_grade = grades_sum / students

print(f'Top students: {percentage_students_above_5:.2f}%')
print(f'Between 4.00 and 4.99: {percentage_students_between_4_and_5:.2f}%')
print(f'Between 3.00 and 3.99: {percentage_students_between_3_and_4:.2f}%')
print(f'Fail: {percentage_students_between_2_and_3:.2f}%')
print(f'Average: {average_grade:.2f}')