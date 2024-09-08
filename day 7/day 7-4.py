import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6

letters = ['ardvark','baboon','camel']

chossen_word = random.choice(letters)

khat = []
for i in chossen_word :
    khat.append('_')
print(khat)    
while lives > 0 and '_' in khat:
    user_word = input("choose world : ")
    vojod = False
    for i in range(len(chossen_word )):
        if user_word == chossen_word[i] : 
            khat[i] = user_word
            vojod = True
    if vojod == False :
        lives -= 1    
    print(khat)   
    print(HANGMANPICS[6-lives])     
if '_' in khat:
    print("you lose! badbakht ")    
else :
    print("you win")    