number_of_people = int(input())
number_of_nights = int(input())
number_of_cards_for_transport = int(input())
number_of_tickets_for_museums = int(input())

price_nights = number_of_nights * 20
price_cards_for_transport = number_of_cards_for_transport * 1.60
price_tickets_for_museums = number_of_tickets_for_museums * 6
total_sum_per_person = price_nights + price_cards_for_transport + price_tickets_for_museums
total_sum_group = total_sum_per_person * number_of_people
end_sum = total_sum_group + total_sum_group * 0.25

print(f'{end_sum:.2f}')