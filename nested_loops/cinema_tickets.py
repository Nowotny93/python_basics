movie = input()

total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0
bought_tickets = 0

while movie != "Finish":
    capacity = int(input())
    type_ticket = input()
    bought_tickets = 0
    while type_ticket != "End":
        total_tickets += 1
        bought_tickets += 1
        if type_ticket == "standard":
           standard_tickets += 1
           if bought_tickets >= capacity:
               break
           type_ticket = input()
        elif type_ticket == "student":
           student_tickets += 1
           if bought_tickets >= capacity:
               break
           type_ticket = input()
        elif type_ticket == "kid":
           kid_tickets += 1
           if bought_tickets >= capacity:
               break
           type_ticket = input()
    percentage_presence = (bought_tickets / capacity) * 100
    print(f'{movie} - {percentage_presence:.2f}% full.')
    movie = input()

percentage_standard = (standard_tickets / total_tickets) * 100
percentage_student = (student_tickets / total_tickets) * 100
percentage_kid = (kid_tickets / total_tickets) * 100
print(f'Total tickets: {total_tickets}')
print(f'{percentage_student:.2f}% student tickets.')
print(f'{percentage_standard:.2f}% standard tickets.')
print(f'{percentage_kid:.2f}% kids tickets.')