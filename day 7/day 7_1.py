import random
names = ["ardvark","baboon","camel"]
name = random.choice(names)
print(list(name))
guess = input("have a guess :").lower()
# print(guess)
Result = "No"
for char in name :
    if guess == char :
        Result= "Yes"    
print (Result)        