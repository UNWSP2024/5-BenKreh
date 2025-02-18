#Ben Krehbiel
#2/27/2025
#did you do your math homework?



import random as rn
import operator

operator_functions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

operators = ["+", "-", "*", "/"]
correct = 0
wrong = 0

def get_question():
    global correct
    global wrong
    for i in range(5):
        rn_op = rn.choice(operators)
        n1 = rn.randint(1, 1000)
        n2 = rn.randint(1, 1000)

        print(f'What is: {n1} {rn_op} {n2}?')

        result = operator_functions[rn_op](n1, n2)
        rounded_result = round(result, 2)
        try:
            user_input = float(input("Please enter your answer (round to 2 decimal places if needed): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_input == rounded_result:
            print("That is correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {rounded_result}.")
            wrong += 1

def yippie():
    global correct
    global wrong
    print("You got ", correct, "right", "and", wrong, "wrong")


get_question()
yippie()
