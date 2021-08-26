number = int(input())

combinations = 0

for i in range(number+1):
    for j in range(number+1):
        for z in range(number+1):
            if i + j+ z == number:
                combinations += 1

print(combinations)
