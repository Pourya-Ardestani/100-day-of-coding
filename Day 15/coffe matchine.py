# Pourya Ardestani Day 15  1402/11/20
from random import randint
import logos
from Data import Cafe


def check_resources(resources, cafe_type):
    if Resources["Water"] < Cafe[cafe_type]["Water"]:
        return "Water"
    elif Resources["Coffee"] < Cafe[cafe_type]["Coffee"]:
        return "Coffee"
    elif Resources["Milk"] < Cafe[cafe_type]["Milk"]:
        return "Milk"
    else :
        return ""


def Report(Resource, Money):
    print(f"Water: {Resource['Water']} ")
    print(f"Coffee: {Resource['Coffee']}")
    print(f"Milk: {Resource['Milk']} ")
    print(f"Money: {Money} ")


def Daryaft_pol():
    print("Please enter coins :")
    quarters = int(input("How many quarters?: "))
    dims = int(input("How many dims?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.01) + (dims * 0.1) + (nickles * 0.05) + (pennies * 0.25)


def resource_decrease(user_choice, coins, Money):
    Resources["Water"] -= Cafe[user_choice]["Water"]
    Resources["Coffee"] -= Cafe[user_choice]["Coffee"]
    Resources["Milk"] -= Cafe[user_choice]["Milk"]
    Money += Cafe[user_choice]["Cost"]
    return coins - Cafe[user_choice]["Cost"], Money



Resources = \
    {
        "Water": randint(100, 400),
        "Coffee": randint(30, 100),
        "Milk": randint(90, 200),
    }
Money = 0.0
end = False
print(logos.start)
while not end:
    print("psssssssst :")
    Report(Resources, Money)
    service = input("What would you like? (espresso /latte/cappuccino):").lower()

    if service == "report":
        Report(Resources, Money)
    elif service == "off":
        end = True
    else:
        check = check_resources(Resources, service)
        if check != "":
            print(f"Sorry there is not Enough {check}")
            continue
        else:
            coins = Daryaft_pol()
            if coins < Cafe[service]["Cost"]:
                print("Sorry there is not Enough Money . Money refunded")
                continue
            else :
                remain_coins, Money_ezaf = resource_decrease(service, coins ,Money)#money decreases and decrease resources
                Money += Money_ezaf
                print(f"here is your {service} 💩💩💩💩💩")
                print(f"Here is your remain {remain_coins}")



