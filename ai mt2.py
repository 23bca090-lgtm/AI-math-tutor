import random

score = 0

for i in range(5):
    a = random.randint(1,10)
    b = random.randint(1,10)

    answer = int(input(f"{a} x {b} = "))

    if answer == a*b:
        print("Correct!")
        score += 1
    else:
        print("Wrong. Answer:", a*b)

print("Final Score:", score)