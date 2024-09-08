import random
names = input("names :").split(', ')
print(len(names))
loser_number = random.randint(0,len(names)-1)
loser = names[loser_number]
print(f"{loser} is gona pay today's meal")