order = {}
def shopping_cart():
   global order

   while True:
         # print current order
      if order:
         print("\nYour current cart items : ")
         for items, price in order.items():
               print(f"{items.capitalize()} - ${price}")

      food = input("\nEnter the food item you want (or 'done' to finish) : ").lower()
      # check point
      if food == "done":
         print("Thanks for Shopping !!")
         break
      try:
         price = float(input(f"Enter the price of {food.capitalize()} : $"))
         if price < 0:
            print("price can't be negative")
         order[food] = price
         
      except ValueError:
         print("Invalid price. Please enter a valid number.")

         print(order)
   if order:
            total_price = sum(order.values())
            print("\nYour final order:")
            for items, price in order.items():
                  print(f"{items.capitalize()} - ${price:.2f}")
            print(f"Total Price: ${total_price:.2f}")
         
shopping_cart()