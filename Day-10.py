# #Day-10
# #10.1

# def format_name(f_name, l_name ):
#   fro_f_name =f_name.title()
#   for_l_name =l_name.title()
#   return f"{fro_f_name} {for_l_name}"


# print(format_name("rohit","khadka"))


# #10.2
# def format_name(f_name, l_name ):
  
#   if f_name =="" and l_name == "":
#     return "You have not give the input " 

#   fro_f_name =f_name.title()
#   for_l_name =l_name.title()
#   return f"{fro_f_name} {for_l_name}"
#   #print("hello")--doesnot work after the return statement


# print(format_name(input("Enter your f_name"),input("Enter your Last name")))


# !0.4
#Building Calculator
import os 

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

#Add
def add(n1, n2):
    return n1+n2

#Sub
def sub(n1, n2):
    return n1-n2

#Mul
def mul(n1, n2):
    return n1*n2

#div
def div(n1, n2):
    return n1/n2


operation = {"+":add,
 "-":sub,
 "*":mul,
 "/":div}

def calculator():
  num1 = float(input("Enter the first num:"))


  for symbol in operation:
    print(symbol)

  should_cont = True
  while should_cont:
    operation_sym = input("Enter the operation that you wanna do :")
    num2 = float(input("Enter the second  num:"))
    calc_fun = operation[operation_sym]
    answer = calc_fun(num1,num2)

    print(f"{num1} {operation_sym} {num2} = {answer}")

    option = input("do you want to continue? yes / no :")

    if option == "no":
      should_cont = False
      os.system('cls')
      calculator()
    else:
      num1 = answer

calculator()