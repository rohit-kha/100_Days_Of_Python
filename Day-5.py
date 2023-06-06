#5.1
#avg height 
sum = 0
s_height = input("Input a list of students heights :").split()
for n in range(0,len(s_height)):
    s_height[n]= int(s_height[n])

print(s_height)

for n in s_height:
    sum = sum + n

print(sum)

avg_height = sum/len(s_height)
print(avg_height)

#5.2
#max score

s_marks = input("Input a list of students marks :").split()
for n in range(0,len(s_marks)):
    s_marks[n]= int(s_marks[n])

print(s_marks)
max_score = max(s_marks)
print(max_score)


#5.3.
#adding only evens
sum = 0
for i in range(2,101,2):
    sum = sum + i
print(sum)

#5.4.
#FizzBuzz
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i% 5== 0:
        print("Buzz")
    else:
        print(i)

#5.5
#Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
password = ""
for char in range(0,nr_letters+1):
    password += random.choice(letters)
for char in range(0,nr_symbols+1):
    password += random.choice(symbols)
for char in range(0,nr_numbers+1):
    password += random.choice(numbers)

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
2
password_list = []
for char in range(0,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(0,nr_numbers+1):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)
print(password_list)

passwo= ""
for i in password_list:
    passwo += i 
print(passwo)