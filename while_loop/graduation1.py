name = input()

years = 1
grade_sum = 0
failures = 0
successfull_graduation = True

while years <= 12:
    grade = float(input())
    if grade < 4:
        failures += 1
        if failures > 1:
            successfull_graduation = False
            break
        continue
    grade_sum += grade
    years += 1
average_grade = grade_sum / 12

if successfull_graduation:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{name} has been excluded at {years} grade')