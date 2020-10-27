import random

def roll(min, max):
    while True:
           print("Rolling the dices...")
           print(f"Your number is {random.randint(min, max)}")
           answer = input("Do you want to roll the dices again? (y/n) ")
           if answer.lower() == 'n':
            break
           elif answer.lower() != 'n' and answer.lower() != 'y':
                print("Please Enter y/n ")
roll(1, 6)  