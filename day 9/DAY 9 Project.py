from gavel_logo import logo 
import os
print(f"hello welcome to the bidering! \n {logo}")

biders = {}
end = False
while(not end):
    Name = input("what is your Name? : ")
    bid_price = input("how many do you want to bid ? : $")
    biders[Name]=int(bid_price)

    countinue = input("is there anyone else to bid ?(YES Or NO) :")
    if countinue=="NO":
        end = True
    else :
       os.system('cls') # on windows 
max = biders[Name]
winner  = Name
for person in biders :
    if biders[person] > max :
        max =  biders[person]
        winner = person

print(f"the winner is {winner} with the price of {max}$")
