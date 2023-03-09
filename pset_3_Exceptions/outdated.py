menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def user_dish_choice():
    sum_of_prices = 0.0
    while True:
        try:
            user_choice = input("Item: ").title()
            if user_choice in menu:
                sum_of_prices = dish_price_count(menu, user_choice, sum_of_prices)
                print(f"Total: ${sum_of_prices:.2f}")
        except EOFError:
            break


def dish_price_count(menu, user_choice, sum_of_prices):
    price = menu.get(user_choice)
    sum_of_prices += price
    return sum_of_prices


user_dish_choice()
