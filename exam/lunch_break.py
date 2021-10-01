import math

series_name = input()
time_of_episode = int(input())
total_time_of_break = int(input())

time_for_lunch = (1 / 8) * total_time_of_break
time_for_rest = (1 / 4) * total_time_of_break
left_time = total_time_of_break - time_for_lunch - time_for_rest

if left_time >= time_of_episode:
    left_time_after_episode = left_time - time_of_episode
    print(f"You have enough time to watch {series_name} and left with {math.ceil(left_time_after_episode)} minutes free time.")
else:
    needed_time = time_of_episode - left_time
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(needed_time)} more minutes.")