#Day-9
#Dictionary

s_score = {"Rohit":93,
           "Subarna":76,
           "Silon":79,
           "Bharat":88 }
print(s_score)
s_nscore ={}
for key in s_score:
    if s_score[key] > 90 and s_score[key] <101:
        s_nscore[key] = "Outstanding"
    elif s_score[key]> 80:
        s_nscore[key] = "Exceed Expectation"
    elif s_score[key] > 70:
        s_nscore[key] = "Acceptable"
    else:
        s_nscore[key] = "Failed"
    
print(s_nscore)

#9.2
#nested dictionary

#nesting dictionary in dictionary
travel_log = {
    "France":{"cities_visited":["Paris","lille","Dijon"],"total_visted":3},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"], "Total_visited":3}
}

print(travel_log)

#nesting disctionary in list

travel_log = [
    {"country":"France",
     "cities_visited":["Paris","lille","Dijon"],
    "total_visted":3},
    {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"], 
    "Total_visited":3}
]

print(travel_log)

#9.3

travel_log = [
    {"country":"France",
     "cities_visited":["Paris","lille","Dijon"],
    "Total_visted":3},
    {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"], 
    "Total_visited":3}
]

def add_new_country(country,cities_visited,Total_visted):
    new_country = {}
    new_country["country"] = country
    new_country["cities"] = cities_visited
    new_country["visits"] = Total_visted
    travel_log.append(new_country)
   

add_new_country("Russia",["Moscow","Saint Peris"],2)
print(travel_log)


#9.4
#Blind Auction
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print()

bid = {}

def highest_bidder (bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
       bid_amt = bidding_record[bidder]
       if bid_amt > highest_bid:
         highest_bid = bid_amt
         winner = bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}")


bidding_finished = False
while not bidding_finished:
   name = input("Enter your name:")
   price = int(input("What is your bid? $"))
   bid[name] = price
   should_continue = input("Are there anyone to bid?")
   if should_continue == "no":
      bidding_finished = True
      print(bid)
      highest_bidder(bid)
   elif should_continue == "yes":
      os.system('cls')
      


