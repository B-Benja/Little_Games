MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(MENU)
# print(MENU["latte"]["ingredients"]["water"])


def resource_check():
    """check if entries in resource dictionary are enough"""
    for ingredient in MENU[user_choice]["ingredients"]:
        for keys in resources:
            if ingredient == keys and MENU[user_choice]["ingredients"][ingredient] >= resources[keys]:
                return False


def resource_deduction():
    """subtract the chosen beverage"""
    for ingredient in MENU[user_choice]["ingredients"]:
        for keys in resources:
            if ingredient == keys:
                 resources[keys] -= MENU[user_choice]["ingredients"][ingredient]


def report():
    """give an overview of the resource dictionary and money variable"""
    for key, value in resources.items():
        print(f"{key}: {value}")
    print(f"Money: {money}")


def turn_off():
    """turn of code"""
    print("Machine shutting down. Have a nice day!")
    return False


machine_running = True
money = 0

while machine_running:
    user_choice = input("What would you like to drink? (espresso/latte/cappuccino)\n").lower()
    if user_choice == 'report':
        report()
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        if resource_check() == False:
            print("Sorry, the machine is empty.\nWe messaged an employee to refill the machine.")
            machine_running = turn_off()
        else:
            print(f"{user_choice.title()} costs {MENU[user_choice]['cost']}. Please enter the amount of coins:")
            quarters = float(input("No. of quarters: "))
            dimes = float(input("No. of dimes: "))
            nickles = float(input("No. of nickles: "))
            pennies = float(input("No. of pennies: "))
            payment = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if payment < MENU[user_choice]['cost']:
                print('Sorry that is not enough money!')
            else:
                resource_deduction()
                money += MENU[user_choice]['cost']
                print(f"First you get your change back: ${round(payment - MENU[user_choice]['cost'],2)}\nNow we brew a beautiful fresh {user_choice.title()}")
                print(f"Here is your {user_choice.title()}. Enjoy!")
    elif user_choice == 'exit':
        machine_running = turn_off()
    else:
        print("Wrong input.")

