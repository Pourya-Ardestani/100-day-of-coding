import random
choice1 = int(input('PLease Enter a Number as rock "0" papper"1"  scissor"2" : ' ))
computer_choice = random.randint(0,2)
# print(computer_choice)
if choice1==0:
    print("you choose rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice1 ==1 :
    print("you choose papper")
    print("""
     _______
---'    ____)_____
           ________)
          _________)
         _________)
---.____________)
""")
elif choice1 == 2 :
    print("you choose scissor")
    print("""
    ________
---'   _____)____
          _______)
       ____________)
      (______)
---.__(_____)
""")
else :
    print ("what do you choose? out of rang")    
print(" \tand ")
if computer_choice == 0:
    print("computer choose rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


elif computer_choice == 1 :
    print("computer choose papper")
    print("""
     _______
---'    ____)_____
           ________)
          _________)
         _________)
---.____________)
""")


elif computer_choice == 2 :
    print("computer choose scissor")
    print("""
    ________
---'   _____)____
          _______)
       ____________)
      (______)
---.__(_____)
""")
else :
    print ("ERROR")    


if choice1-computer_choice == 1 or choice1 - computer_choice==-2 :
    print("you win  :)!!!")
elif choice1-computer_choice == 0 :
    print ("draw !!!")
else : 
    print("you lose :(")    
 
