n = int(input())

correct = False
for thousands in range(1, 10):
    for hundreds in range(1, 10):
        for tens in range(1, 10):
            for units in range(1, 10):

              if (units + tens) == (hundreds + thousands) and n % (units + tens) == 0:
                  correct = True

                  if correct:
                    print(f"{thousands}{hundreds}{tens}{units}", end=" ")