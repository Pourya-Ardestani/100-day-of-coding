import random
import logo
import os
from data import Data


print(logo.higher_or_lower)

def p(A,B):
    print(f"compare A: {A['name']} , a {A['info']}, from {A['country']}")
    print(logo.Vs)
    print(f"compare B: {B['name']} , a {B['info']}, from {B['country']}")


def play_Game(a_dict , b_dict):
    global lose

    p(a_dict,b_dict)
    a_number = a_dict['folower']
    b_number = b_dict['folower']
    dict_choose = {'A':a_number,'B':b_number}
    user_choice  = input("who has more folowers? Type 'A' or 'B': ")
    user_number = dict_choose[user_choice]
    if  user_number < a_number and user_number < b_number :
        return True




First_dict = random.choice(Data)
score = 0
lose = False
while not lose :
    second_dict =random.choice(Data)
    lose = play_Game(First_dict,second_dict)
    score +=1 
    First_dict = second_dict
    os.system('cls')
    print(f"your score is : {score}")
    
print (f"you lose with the score of{score}")