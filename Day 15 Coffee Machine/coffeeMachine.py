from menu import MENU, resources

money = 0

def checkResources(resources,coffee):
    for i in MENU[coffee]['ingredients']:
        if resources[i] - MENU[coffee]['ingredients'][i] < 0:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def printReport(money):
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == 'off':
        break
    elif coffee == 'report':
        printReport(money)
        continue

    quaters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = 0.25*quaters + 0.1*dimes + 0.05*nickles +0.01*pennies

    cost = MENU[coffee]['cost']

    if total >= cost:
        if checkResources(resources,coffee):
            print(f"Here is ${total-cost} in change.")
            print(f"Here is your {coffee}. Enjoy!")
            for i in MENU[coffee]['ingredients']:
                resources[i] -= MENU[coffee]['ingredients'][i]
            money += cost
    else:
        print("Sorry that's not enough money. Money refunded.")