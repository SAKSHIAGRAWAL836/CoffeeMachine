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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns true if you have enough resources to make the drink, otherwise returns False."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def calculate_money():
    """Returns the total money given."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return money

def is_money_sufficient(money_paid, drink_cost):
    """Returns true if money received is enough and also returns the change. Returns False otherwise."""
    if money_paid >= drink_cost:
        change = round(money_paid - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough coins.")
        return False

def make_coffee(drink_name, order_ingredients):
    """takes drink order and deducts the item from resources used."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
    
is_on = True

while is_on:
    #Take input from user
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":      #to switch off the coffee machine
        is_on = False
        
    elif user_input == 'report':         #to check what and how much resources is left and profit
        water_left = resources['water']
        milk_left = resources['milk']
        coffee_left = resources['coffee']
        profit_made = profit
        print(f'Water = {water_left}ml\nMilk = {milk_left}ml\nCoffee = {coffee_left}g\nMoney = ${profit_made}')
        
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = calculate_money()
            if is_money_sufficient(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])


