import math

income = float(input())
average_grade = float(input())
minimum_wage = float(input())

if income > minimum_wage:
    print("You cannot get a scholarship!")
elif income < minimum_wage and average_grade > 4.5 :
    social_scholarship = math.floor(minimum_wage * 0.35)
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif average_grade > 5.50 :
    excellent_grade_scholarship = math.floor(average_grade * 25)
    print(f'You get a scholarship for excellent results {excellent_grade_scholarship} BGN')
elif income < minimum_wage and average_grade > 5.5:
    excellent_grade_scholarship = math.floor(average_grade * 25)
    print(f'You get a scholarship for excellent results {excellent_grade_scholarship} BGN')