order = {}

def shopping_cart():
    while True:
        # print current order
        if order:
           print("\nYour current orders : ")
           for items, price in order.items():
                print(f"{items.capitalize()} - ${price}\n")

        food = input("Enter the food item you want (or 'done' to finish) : ").lower()
        # check point
        if food == "done":
         print("Thanks for Shopping !!")
         break

        try:
           price = float(input(f"Enter the price of {food.capitalize()} : $"))
           order[food] = price
        except ValueError:
           print("Invalid price. Please enter a valid number.")

shopping_cart()