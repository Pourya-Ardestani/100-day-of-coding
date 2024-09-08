# BLACK JACK PROJECT
from random import choice, randint
from logo_BlACK_JACK import logo

def check_ACE(card_list , total): # if the ace was in hand andhand go over 21 return the 11 to 1
    leng = len(card_list)
    if total >21 :
        i = 0
        while i<leng:
            if card_list[i] == 11:
                card_list[i]-=10
            i+=1
    return card_list        


def print_carts(total,cards ,pccards):
    print(f"your cards :{cards} \n total :{total}  \ncomputer cards : {pccards} \n")


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print(logo)
#cards[randint(0,12)]
user_cards = [11,cards[randint(0,12)]] 
computer_cards = [cards[randint(0,12)],cards[randint(0,12)]]

# print(user_cards,computer_cards , choice(cards) , sum(user_cards))


print(f"your card : {user_cards} \ncomputers first card : {computer_cards[0]}")
do_continue = "y"
while do_continue == "y" :
    do_continue = input("do you want another card ? (y or n) :")
    if do_continue == 'y':
        user_cards.append(choice(cards))
        user_cards = check_ACE(user_cards,sum(user_cards))
        if sum(user_cards) > 21:
            print(f"YOU lose !! {sum(user_cards)} > 21")
            do_continue = "n"
            
    elif do_continue == 'n':
        end = False
        while not end :   
            if sum(computer_cards) <17:
                computer_cards.append(choice(cards))
                computer_cards = check_ACE(computer_cards,sum(computer_cards))

                if sum(computer_cards)>21:
                    end = True 
                    do_continue = "n"
    print_carts(sum(user_cards),user_cards,computer_cards)               



# dict_l = {}