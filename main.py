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

MONEY = 0

def write_report():
    for resource in resources:
        print(resource + ": " + str(resources[resource]) + "%s" %("ml" if resource == "water" or resource == "milk" else "g" ))
    print("Money: $" + str(MONEY) + "\n")

def check_resources(choice):
    drink = MENU[choice]  # get the drink info from the MENU
    for ingredient, required_amount in drink["ingredients"].items():
        if required_amount > resources.get(ingredient, 0):
            print(f"Sorry, not enough {ingredient}.")
            return False

    return True

def manage_resources():
    still_on = True
    while still_on:
        new_resource = input("What resource do you want to add, water (w), milk (m) or coffee (c). Type 'exit' to leave?: ")
        match new_resource:
            case "w":
                amount = input("How much water do you want to add?: ")
                resources["water"] += int(amount)
            case "m":
                amount = input("How much milk do you want to add?: ")
                resources["milk"] += int(amount)
            case "c":
                amount = input("How much coffee do you want to add?: ")
                resources["coffee"] += int(amount)
            case "exit":
                still_on = False




def process_coins(choice):
    global MONEY
    drink = MENU[choice]
    quarters = input("How many quarters: ")
    dimes = input("How many dimes: ")
    nickels = input("How many nickels: ")
    pennies = input("How many pennies: ")

    total = (int(quarters) * 0.25) + (int(dimes) * 0.1) + (int(nickels) * 0.05) + (int(pennies) * 0.01)
    if total < drink["cost"]:
        print("Sorry, thats not enough money. money refunded")
        return 0


    change = total - drink["cost"]
    MONEY += drink["cost"]
    print(f"Here is ${change:.2f} in change")
    return None

def make_coffee(choice):
    drink = MENU[choice]
    for ingredient, amount in drink["ingredients"].items():
        resources[ingredient] -= amount


    print(f"Here is your {choice} ☕️. Enjoy!")


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        write_report()
    elif choice == "manage":
        manage_resources()
    else:
        if check_resources(choice) == True:
            process_coins(choice)
            make_coffee(choice)
