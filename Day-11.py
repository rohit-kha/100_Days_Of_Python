#CAPSTONE
import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \|Dad |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print()

def deal_card():
  #"retutns random cards from the deck"
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card



def calculate_score(cards):
   """Take a list of cards and return its calculation"""
   if sum(cards) == 21 and len(cards) == 2:
     return 0
   
   if 11 in cards and sum (cards) > 21:
    cards.remove(11)
    cards.append(1)

   return sum(cards)

def comp_score(user_score, dealer_score):
  if user_score == dealer_score:
    return "Draw"
  elif dealer_score == 0:
    return "loose, opponent has the Blackjack"
  elif user_score == 0:
    return "win with a black jack"
  elif user_score >21:
    return "you went over. you loose"
  elif dealer_score > 21:
    return "Opponent went over. You win"
  elif user_score > dealer_score :
    return "You win"
  else:
    return "you loose"
def paly_game():
    user_card = []
    dealer_card =[]

    for _ in range (2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_card)
        dealer_score = calculate_score(dealer_card)
        print(f"your cards: {user_card}, current score: {user_score}")
        print(f"Dealers first cardL: {dealer_card[0]}")

        if user_score == 0 or dealer_score == 0 or user_score >21 :
            is_game_over = True
        else:
            add_another = input("do you want to add another card: 'yes' or ' no' ")
            if add_another == "yes":
             user_card.append(deal_card())
            else:
             is_game_over = True


    while dealer_score != 0 and dealer_score <17:
        dealer_card.append(deal_card)
        dealer_score = calculate_score(dealer_card)


    print(f"your final cards: {user_card}, final score: {user_score}")
    print(f"dealer final cards: {dealer_card}, dealer final score: {dealer_score}")

    print(comp_score(user_score, dealer_score))

another_game = input("Do you want to play  game? yes/no :")
if another_game == "yes":
  os.system('cls')
  paly_game()

