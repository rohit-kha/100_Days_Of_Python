# #2.1
# testnum = input("Enter your number:")

# first_num = testnum[0]
# second_num = testnum[1]

# final = int(first_num)+int(second_num)
# print(final)

# #2.2
# weight = int(input("Enter your weight :"))
# height = float(input("Enter your height :"))

# body_index = weight / (height**2)

# print(int(body_index))

# #2.3.
# age = int(input("Enter your age :"))

# age_remaining = 90 - age
# month_remaining = age_remaining * 12
# week_remaining = age_remaining *52
# days_remaining =age_remaining *365

# message = f"Your have {age_remaining} left/{month_remaining} months left/ {week_remaining}weeks left/ {days_remaining} days left"

# print(message)


#2.4.
#----------------------Tip Calculator----------

print("Welcome to the Tip Calculator")

amt = float(input("What is the total bill? :"))
tip = int(input("What percentage would you like to tip? 10 or 12 0r 15?:"))
people = int(input("How many of you are to pay the bill?:"))

tip_amt = ((amt*tip)/100)
tot_amt = (amt + tip_amt)
each_pay = (tot_amt/people)
final_bill = round(each_pay,2)

message = f"Each of you need to pay: {final_bill}"
print(message)