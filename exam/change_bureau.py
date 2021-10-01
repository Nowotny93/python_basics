bitcoins = int(input())
chinese_joans = float(input())
commission = float(input())

bitcoins_into_levs = bitcoins * 1168
chinese_joans_into_dollars = chinese_joans * 0.15
dollars_into_levs = chinese_joans_into_dollars * 1.76
sum_levs = bitcoins_into_levs + dollars_into_levs
total_levs_into_euros = sum_levs / 1.95
commission = (commission / 100) * total_levs_into_euros
total_euros_after_commission = total_levs_into_euros - commission

print(f'{total_euros_after_commission:.2f}')