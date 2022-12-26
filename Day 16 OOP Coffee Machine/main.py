from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
while True:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == 'off':
        break
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
        continue
    item = menu.find_drink(choice)
    if item:
        if coffeeMaker.is_resource_sufficient(item):
            if moneyMachine.make_payment(item.cost):
                coffeeMaker.make_coffee(item)
