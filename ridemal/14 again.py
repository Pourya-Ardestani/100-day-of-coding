# Pourya ardestani 1402/11/20 friday
# higher or lower game
import os
import logos
from Datas import Data
from random import choice


# print("hello world", end="")
# print(f"salam {Data[0]['name']} ddf")

def compare(A, B):
    if A['Follower'] > B['Follower']:
        print(f"psssssssst {A['name']}")
        return A
    else:
        print(f"psssssssst {B['name']}")
        return B


def ret_follower_choice(C, A, B):
    if C == 'A':
        return A['Follower']
    elif C == 'B':
        return B['Follower']


print(logos.higher_or_lower)
lose = False
score = 0
A = choice(Data)
while not lose:

    B = choice(Data)
    while B == A:
        B = choice(Data)

    print(f"your score is {score}")
    print(f"between  A : {A['name']} ,that is {A['info']} ,from {A['country']}  ")
    print(logos.Vs)
    print(f"And B : {B['name']} ,that is {B['info']} ,from {B['country']}  ")
    user_choice = input("A or B :").upper()
    user_follower = ret_follower_choice(user_choice, A, B)
    if compare(A, B)['Follower'] == user_follower:
        score += 1
        os.system('cls')
        A = compare(A, B)
    else:
        lose = True
    os.system('cls')

print(f"you lose! with score of {score}")
