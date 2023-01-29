from gameart import logo,vs 
import random
from replit import clear
from game_data import data
# Generate a random account from the game data.

def random_data_account():
    return random.choice(data)

def account_formatting(account_data):
    name = account_data["name"]
    description = account_data["description"]
    country = account_data["country"]
    
    return f"{name}, a {description} from {country}" 

def is_correct(user_guess, count_a:int, count_b:int): 
     if count_a > count_b:
         return user_guess == "a"
     else:
         return user_guess == "b"


def play_highlow(): 
    print(logo)
    score = 0   
    game_on = True
    account_b = random_data_account()
    
    while game_on:
        #print(logo)
        account_a = account_b
        account_b = random_data_account()

        count_a:int = account_a["follower_count"]
        count_b:int = account_b["follower_count"]
        print(count_a, count_b)
        print(f"Compare A : {account_formatting(account_a)} ")
        print(vs)
        print(f"Against B : {account_formatting(account_b)} ")

        user_guess = input("Enter Your Choice A or B : ").lower()
        check = is_correct(user_guess, count_a, count_b)
        clear()
        print(logo)
        if check:
            score += 1
            print(f"You are Correct! Your score is {score}")
        else:
            print(f"Your Wrong Your final score is {score}")
            if input("Do you want to play again Game Again ? Type 'y' for Yes 'N' For No : ").lower() == 'y':
               play_highlow() 
            else:
                game_on = False
    
play_highlow()    
# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.