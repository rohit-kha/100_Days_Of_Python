import random
from gameData import data
import os
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
# Dislay art

def format_data(account):
    """Takes the account data and returns the printabke format"""
    acc_name = account['name']
    acc_desc = account['description']
    acc_country = account['country']
    return(f"{acc_name}, a {acc_desc}, from{acc_country}")

def check_answer(guess, a_follower, b_follower):
    """Takes the user dtaa and count if they got right"""
    if a_follower > b_follower:
        return guess =="a"
    else:
        return guess == "b"


print(logo)
score = 0
acc_b = random.choice(data)
Should_cont = True
while Should_cont:
    # Swap the position
    acc_a  = acc_b
    acc_b = random.choice(data)
    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Comapre A: {format_data(acc_a)}")
    print(vs)
    print(f"Comapre A: {format_data(acc_b)}")


            #Ask user for the guess

            #Check if user is correct 
            ##Get follower counted 
            ##use if-else to evaluated
    guess = input ( "Who has more followers ? Type 'A' 'B' :" ).lower()

        

            #Score should be counted 
    a_follower = acc_a['follower_count']
    b_follower = acc_b['follower_count']
    is_correct = check_answer(guess, a_follower, b_follower)


    #Clear account
    os.system('cls')
    print(logo)


    #Give the user feedback
    if is_correct:
        score += 1
        print(f"You are right!! Current score : {score}")
    else:
        Should_cont = False
        print(f"Sorry Thats wrong!! current {score}")
    
      

       

       