import math

series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
time_episode_without_advertisements = float(input())

time_advertisements_per_episode = 0.2 * time_episode_without_advertisements
time_episode_with_advertisements = time_episode_without_advertisements + time_advertisements_per_episode
add_time_from_special_episodes = number_of_seasons * 10
total_time = time_episode_with_advertisements * number_of_episodes * number_of_seasons + add_time_from_special_episodes

print(f'Total time needed to watch the {series_name} series is {math.floor(total_time)} minutes.')