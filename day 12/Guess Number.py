from random import randint
from logo_guess import logo

def position(gnumber):
    if gnumber < NUMBER:
        print("higher ")
    else:
        print("lower ")



def game(chance):
    win = False
    while chance > 0:
        print(f"you have {chance} attempt remaining to guess the number")
        guess = int(input("give your guess :"))
        if guess == NUMBER :
            win = True 
            break
        else:
            position(guess)
        chance -=1
    if not win :
        print("you lose !!😭😢😰")
    else :
        print("you WIN !!!!🤩 🥳🌈✨⚡️")      




print(logo)
print("welcome to the guessing number game : \n im thinking of a number between 1 and 100")


NUMBER = randint(1,100)
dificulty_level = input("hard or easy?")

if dificulty_level == "easy" :
    chances = 10
elif dificulty_level == "hard":   
    chances = 5
game(chances)