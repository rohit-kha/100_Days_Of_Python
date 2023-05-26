from getpass import getpass as input
print("##########################################")
print("Lets Play Rock, Siccors and paper")
print("###########################################")

player1 = input("Give your shot -> R-Rock, S-Scissors and P- Paper :")
player2 = input("Give your shot -> R-Rock, S-Scissors and P- Paper :")

if player1 =="R" and player2 == "S":
  print("\033[32m","Player one wins 🎉")
elif player1 =="S" and player2 =="P":
  print("\033[32m","Player1 wins 🎉 ")
elif player1 =="P" and player2 =="R":
  print("\033[32m","Player1 wins ")
elif player1 =="P" and player2 =="S":
  print("\033[32m","Player2 wins🎉 ")
elif player1 =="S" and player2 =="R":
  print("\033[32m"," player2 wins 🎉")
elif player1 =="R" and player2 =="P":
  print("\033[32m","Player2 wins 🎉")
else:
  print("\033[36m","Invalid Entry 🚫")