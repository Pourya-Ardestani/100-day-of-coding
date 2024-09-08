import random

items = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''' 
         ,'''
_______
---'    ____)_____
           ________)
          _________)
         _________)
---.____________)''' 
         ,'''
  ________
---'   _____)____
          _______)
       ____________)
      (______)
---.__(_____)''' ,]


u_choice = int(input("please Enter number 0 for rov.1 2........"))
c_choice = random.randint(0,2)
if u_choice >2 or u_choice <0 :
    print("invalid number")

else :
    print(f"you choose \n\n {items[u_choice]}")
    print(f"\n\nand computer choose \n\n{items[c_choice]}\n")
    if u_choice - c_choice ==1 or u_choice - c_choice ==-2 :
        print("you win  🎊 🎉 !!!!")
    elif u_choice == c_choice :
        print("draw")
    else :
        print("you lose ! :(")    

