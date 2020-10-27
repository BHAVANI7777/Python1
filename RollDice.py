import random

def roll(min, max):
    while True:
            answer = input("Do you want to roll the dices ? (y/n) ")
            if answer.lower() == 'n':
                break
            elif answer.lower() != 'n' and answer.lower() != 'y':
                print("Enter valid letter...")
            else:
                print("Rolling the dices...")
                print(f"Your number is {random.randint(min, max)}")


roll(1, 6)
