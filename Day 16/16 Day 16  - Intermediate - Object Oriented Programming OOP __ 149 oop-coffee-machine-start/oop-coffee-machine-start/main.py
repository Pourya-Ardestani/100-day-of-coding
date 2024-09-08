from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# latte = MenuItem("latte", 200, 24, 150, 2.5)
# espresso = MenuItem("espresso", 200, 24, 150, 2.5)
# cappuccino = MenuItem("cappuccino", 200, 24, 150, 2.5)

money = MoneyMachine()
end = False
coffeeMaker = CoffeeMaker()
menu = Menu()
while not end:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "report":
        coffeeMaker.report()
        money.report()
        continue
    elif choice == "off":
        break
    item_menu = menu.find_drink(choice)
    if coffeeMaker.is_resource_sufficient(item_menu):
        if money.make_payment(item_menu.cost):
            coffeeMaker.make_coffee(item_menu)


