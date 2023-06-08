import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo) 
lives = 6                                                                   
                                                                    
l_words = ["Apple", "Banana", "Orange"]

s_word = random.choice(l_words).lower()
w_len = len(s_word)

display = []
for letter in range (w_len):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    g_word = input("Guess the letter ").lower()
    for position in range(w_len):
      lett = s_word[position]
      if lett == g_word:
         display[position] = lett
    print(display)
    if g_word not in s_word:
      lives -= 1
      if lives == 0 :
        end_of_game = True
        print("You loose")
    print(f"{' '.join(display)}")
    if "_" not in display:
      end_of_game = True
      print("You win")

    print(stages[lives])




