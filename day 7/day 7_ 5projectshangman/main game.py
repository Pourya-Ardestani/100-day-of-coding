import random
import os
import stages , time
import hangman_letters
import hangman_logo
print(hangman_logo.logo)

lives = 6

chossen_word = random.choice(hangman_letters.words)

khat = []
chosen_list=[]
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

    if user_word in chosen_list :
        print("that was tekrari ")
    else :    
        if vojod == False :
            lives -= 1 
            print("that letter was not in the choosen word")       

    print(khat)   
    print(stages.stage[6-lives]) 
    chosen_list.append(user_word) 
    time.sleep(3)
    os.system('cls')

if '_' in khat:
    print("you lose! badbakht ")    
else :
    print("you win")    