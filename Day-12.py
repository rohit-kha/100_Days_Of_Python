import random

logo = """_____                                           __                             ______                                          
 /      \                                         |  \                           /      \                                         
|  $$$$$$\ __    __   ______    _______   _______  \$$ _______    ______        |  $$$$$$\  ______   ______ ____    ______        
| $$ __\$$|  \  |  \ /      \  /       \ /       \|  \|       \  /      \       | $$ __\$$ |      \ |      \    \  /      \       
| $$|    \| $$  | $$|  $$$$$$\|  $$$$$$$|  $$$$$$$| $$| $$$$$$$\|  $$$$$$\      | $$|    \  \$$$$$$\| $$$$$$\$$$$\|  $$$$$$\      
| $$ \$$$$| $$  | $$| $$    $$ \$$    \  \$$    \ | $$| $$  | $$| $$  | $$      | $$ \$$$$ /      $$| $$ | $$ | $$| $$    $$      
| $$__| $$| $$__/ $$| $$$$$$$$ _\$$$$$$\ _\$$$$$$\| $$| $$  | $$| $$__| $$      | $$__| $$|  $$$$$$$| $$ | $$ | $$| $$$$$$$$      
 \$$    $$ \$$    $$ \$$     \|       $$|       $$| $$| $$  | $$ \$$    $$       \$$    $$ \$$    $$| $$ | $$ | $$ \$$     \      
  \$$$$$$   \$$$$$$   \$$$$$$$ \$$$$$$$  \$$$$$$$  \$$ \$$   \$$ _\$$$$$$$        \$$$$$$   \$$$$$$$ \$$  \$$  \$$  \$$$$$$$      
                                                                |  \__| $$                                                        
                                                                 \$$    $$                                                        
                                                                  \$$$$$$  """

print(logo)
print()

easy_level = 10
hard_level = 5

def check_ans(user_guess, answer,turns):
    """checks answer"""
    if user_guess > answer :
        print("To high")
        return turns -1
    if user_guess < answer :
        print ("To low")
        return turns -1
    else:
        print(f"You got it, {answer}")


def level_diffculty():
    level = input("Choose difficulty level: 'Hard' 'easy'").lower()
    if level == "easy":
        return easy_level
    else:
        return hard_level
def game():
    print("Welcome to the guessing game ")
    print("I m thinking of number betwwen 1-100 :")

    answer = random.randint(1,100)
    print(answer)

    turns = level_diffculty()
    
    user_guess = 0
    while user_guess != answer:
      user_guess = int(input("Enter your guess :"))
      turns = check_ans(user_guess,answer,turns)
      print(f"you have {turns} attempts to guess the number ::")

      if turns == 0:
          print("You loose, out of turns")
          break
      elif user_guess != answer:
          print("You can do it guess again")


game()



# print("Welcome to the guessing game ")
# print("I m thinking of number betwwen 1-100 :")
# level = input("Choose difficulty level: 'Hard' 'easy'").lower()
# if level =="easy":
#    lives = 10
# else:
#    lives = 5

# def check_lives():
#    if 

   

                                                                 
# s_word = random.randint(1,100)

# # def user_input():
# #    return int(input("Enter your guess :"))

# should_cont  = True

# while should_cont :
#    user_guess = int(input("Enter your guess :"))
#    result = check_guess(s_word,user_guess)

#    if lives == 0 or s_word == user_guess:
#       should_cont = False
