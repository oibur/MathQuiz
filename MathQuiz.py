import random

def main():
    score = 0
    while True:
        old_score = score
        game = op_choice()
        score += game
        if score == old_score:
            break
        else:
            print(f'Current score is: {score}')
    print(f'Final score was: {score}')

def op_choice():
    choice = random.randint(1,4)
    if choice == 1:
        return add_ques()
    elif choice == 2:
        return sub_ques()
    elif choice == 3:
        return mul_ques()
    else:
        return div_ques()

def div_ques():
    num1 = 1
    num2 = 2
    while num1 % num2 != 0:
        num1 = random.randint(1,100)
        num2 = random.randint(1,num1)
    answer = num1 / num2
    guess = int(input(f'{num1} / {num2} = '))
    if guess == answer:
        print(f'Correct! {num1} / {num2} = {answer}')
        return 1
    else:
        print(f'Incorrect: {num1} / {num2} = {answer}')
        return 0

def mul_ques():
    num1, num2 = random.randint(1,10), random.randint(1,10)
    answer = num1 * num2
    guess = int(input(f'{num1} * {num2} = '))
    if guess == answer:
        print(f'Correct! {num1} * {num2} = {answer}')
        return 1
    else:
        print(f'Incorrect: {num1} * {num2} = {answer}')
        return 0

def sub_ques():
    num1 = random.randint(1,100)
    num2 = random.randint(1,num1)
    answer = num1 - num2
    guess = int(input(f'{num1} - {num2} = '))
    if guess == answer:
        print(f'Correct! {num1} - {num2} = {answer}')
        return 1
    else:
        print(f'Incorrect: {num1} - {num2} = {answer}')
        return 0

def add_ques():
    num1, num2 = random.randint(1,100), random.randint(1,100)
    answer = num1 + num2
    guess = int(input(f'{num1} + {num2} = '))
    if guess == answer:
        print(f'Correct! {num1} + {num2} = {answer}')
        return 1
    else:
        print(f'Incorrect: {num1} + {num2} = {answer}')
        return 0

if __name__ == '__main__':
    main()