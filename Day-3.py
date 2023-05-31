# 3.1
# Odd/Even
number =int(input("Enter the number :"))

if (number % 2 == 0):
    print("EVEN")
else:
    print("ODD")



# 3.2
# Bmi
weight = float(input("Enter your weight :"))
height = float(input("Enter your height :"))

bmi = round(weight/(height**2),2)

print(f"your BMI is :{bmi}")
print("As per your BMI, you are :")

if bmi <18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
elif bmi <35:
    print("Obese")
else:
    print("Clinically obese")


# 3.3
# Finding a leap year 

print("LEAP YEAR DETECTOR ")

year = int(input("Enter the year you want to test:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: 
            print("It is  a leap year!!!")
        else:
            print("Not a leap year")
    else:
        print("it is  a leap year")

else:
    print("It is not a leap year!!!")

# 3.4
# Pizza 

print("Welcome to Pizza Hub")
print("////////////////////////")
bill = 0
size = input("Enter the size of pizza you want to order:'S' 'M' 'L' :")
peproni = input ("Do you want to add peproni in your pizza? 'Y' 'N' :")
extra_cheese = input("Do you want to add cheese in your pizza? 'Y' 'N' :")

if size == "S":
    bill += 15

elif size == "M":
    bill += 20


elif size == "L":
    bill += 25
else:
    print("We dont have it !!!!!!!!!!")


if peproni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill = bill


if extra_cheese == "Y":
    bill += 1
else:
    bill = bill

print(f"Your Total Bill: {bill}")


#3.5.
#LOVE CALCULATUR
name1 = input("Enter your name:")
name2 = input("Enter your partner name:")

com_name = name1+ name2
lower_case =com_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v= lower_case.count("v")
e= lower_case.count("e")

love = l + o + v + e


total = str(true)+str(love)
final_score = int(total)


if (final_score < 10) or (final_score >90):
    print(f"Your score is {final_score}, you guys are perfect")
elif (final_score >= 40) and (final_score <= 50):
    print(f"Your score is {final_score}, you guys can continue")
else:
    print(f"Your Score is {final_score}")


#Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

road = input("Which road you wanna go ? 'left' or 'right' :")

if road == "left":
    swim = input("Do you want to 'Swim' or 'Wait'? :")
    if swim == "swim":
        print("Game Over")
    else:
        door = input("Choose one door: 'Red' 'yellow' 'blue' :")
        if door == "Red":
            print("Game Over")
        elif door == "blue":
            print("Game Over")
        elif door == "yellow":
            print("Congratch! You win")
        else:
            print("Invalid")
else:
    print("Game Over")            
