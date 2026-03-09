import random

operators = ["+","-","*"]

for i in range(5):
    a = random.randint(1,20)
    b = random.randint(1,20)
    op = random.choice(operators)

    question = f"{a} {op} {b}"
    answer = int(input(question + " = "))

    if answer == eval(question):
        print("Correct")
    else:
        print("Wrong")