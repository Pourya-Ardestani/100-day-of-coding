import random
letters = ['ardvark','baboon','camel']
choosen = random.choice(letters)
print(f"psssst , the choosen is {choosen}")
display = []
for i in range(len(choosen)):
    display.append('_')

while '_' in display:
    count = 0
    guess = input("guess :")
    for char in choosen:
        if guess == char :
            display[count] = char
        count +=1 
    print(display)    

print("you won!")
