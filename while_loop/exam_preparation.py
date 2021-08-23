number_not_satisfying_grades = int(input())

sum_not_satisfying_grades = 0
sum_grades = 0
sum_grades1 = 0
last_poblem = ''
end = True

while sum_not_satisfying_grades < number_not_satisfying_grades:
    name_of_task = input()
    if name_of_task == "Enough":
        end = True
        break
    grade = int(input())
    if grade <= 4:
        end = False
        sum_not_satisfying_grades += 1
    sum_grades += grade
    sum_grades1 +=1
    last_poblem = name_of_task

average_score = sum_grades / sum_grades1
if end:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {sum_grades1}')
    print(f'Last problem: {last_poblem}')
else:
    print(f'You need a break, {sum_not_satisfying_grades} poor grades.')

