#DAY-4
#4.1
#HEAD or TAILS

import random

test_seed = int(input("Enter your test number :"))
random.seed(test_seed)

test_coin = random.randint(0,1)

if test_coin == 1:
    print("Head")
else: 
    print("Tails")


#4.1.
#Pay the Bill
import random

test_seed = input("Enter the test number :")
random.seed(test_seed)

name_input = input("Enter your Friends name:")
name_list = name_input.split(",")

no_of_items = len(name_list)

random_choice = random.randint(0,no_of_items-1)

pay_name = (name_list[random_choice])

print(f"the bill will be paid by {pay_name}")



#4.3
#Treasure Game 
row1 = ['🟥','🟥','🟥']
row2 = ['🟥','🟥','🟥']
row3 = ['🟥','🟥','🟥']

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input ("Enter the position where you want to hide the treasure: ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "T"

print(f"{row1}\n{row2}\n{row3}")

# 4.4.
#Rock-Paper-Scissor
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user1 = input("Give your shot: R, P, S")

if user1 == "R":
    user1_choice = rock
    print(rock)
elif user1 == "P":
    user1_choice = paper
    print(paper)
elif user1 == "S":
    user1_choice = scissors
    print(scissors)
else:
    print("Invalid Input")

test_seed = input("Enter the test number :")
random.seed(test_seed)

user2 = random.randint(1,3)

if user2 == 1:
    user2_choice = rock
    print(rock)
elif user2 == 2:
    user2_choice = paper
    print(paper)
elif user2 == 3:
    user2_choice = scissors
    print(scissors)
else:
    print("Invalid input")


if user1_choice == rock and user2_choice == scissors:
    print("User1 wins")
elif user1_choice == scissors and user2_choice == paper:
    print("User1 wins")
elif user1_choice == paper and user2_choice == rock:
    print("User1 wins")
elif user1_choice == paper and user2_choice == scissors:
    print("User2 wins")
elif user1_choice == scissors and user2_choice == rock:
    print("User2 wins")
elif user1_choice == rock and user2_choice == paper:
    print("User2 wins")
else:
    print("Draw, Try Again ")