class CoffeeMachine:
    def __init__(self, resources, drinks):
        self.resources = resources
        self.drinks = drinks
        self.profit = 0

    def check_resources(self, drink):
        for ingredient, quantity in self.drinks[drink]["ingredients"].items():
            if self.resources[ingredient] < quantity:
                return False
        return True

    def process_order(self, drink, coins):
        cost = self.drinks[drink]["cost"]
        if coins < cost:
            print(f"Sorry, that's not enough money. Money refunded.")
            return 0
        change = round(coins - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        self.resources = {ingredient: self.resources[ingredient] - quantity for ingredient, quantity in self.drinks[drink]["ingredients"].items()}
        print(f"Here is your {drink}. Enjoy!")
        return change

    def handle_order(self, drink):
        if not self.check_resources(drink):
            print("Sorry, there are not enough resources to make this drink.")
            return

        print("Please insert coins:")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))

        total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
        change = self.process_order(drink, total)
        self.profit += change

    def show_report(self):
        print("--- Report ---")
        for resource, quantity in sorted(self.resources.items()):
            print(f"{resource.capitalize().ljust(12)}: {quantity}ml")
        print(f"Money: ${self.profit:.2f}")

    def run(self):
        while True:
            drink_choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
            if drink_choice == "off":
                break
            elif drink_choice == "report":
                self.show_report()
            elif drink_choice in self.drinks:
                self.handle_order(drink_choice)
            else:
                print("Invalid choice. Please choose a valid drink or type 'off' to shut down the coffee machine.")

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

drinks = {
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

coffee_machine = CoffeeMachine(resources, drinks)
coffee_machine.run()
