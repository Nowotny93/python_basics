import math
time1 = int(input())
time2 = int(input())
time3 = int(input())
sum = time1 + time2 + time3
minutes = sum / 60
seconds = sum % 60
minutes = math.floor(minutes)
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')