# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:

# Ask the customer from which menu category they want to order
  print("From which menu would you like to order?")
 
 # Create a variable for the menu item number
  i = 1
 # Create a dictionary to store the menu for later retrieval
  menu_items = {}

  # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
  # Store the menu category associated with its menu item number
  # Add 1 to the menu item number
  for key in menu.keys():
    print(f"{i}: {key}")
    menu_items[i] = key
    i += 1
 # Get the customer's input
  menu_category = input("Enter your menu number: ")
 # Check if the customer's input is a number
  if menu_category.isdigit():
    menu_category = int(menu_category)
    # Check if the customer's input is a valid option
     # Save the menu category name to a variable
     # Print out the menu category name they selected
     # Print out the menu options from the menu_category_name

    if menu_category in menu_items:
      menu_category_name = menu_items[menu_category]
      print(f"You selected {menu_category_name}")

      print(f"What {menu_category_name} item would you like to choose?")

      i = 1
      menu_items = {}
     # Check if the menu item is a dictionary to handle differently
      for key, value in menu[menu_category_name].items():
        if type(value) is dict:
          for key2, value2 in value.items():
            num_spaces = 24 - len(key + key2) - 3
            spaces = " " * num_spaces
            print(f"{i} | {key} - {key2}{spaces} | ${value2}")
            menu_items[i] = {
              "Item name": key + " - " + key2,
              "Price": value2
            }
            i += 1
        else:
          num_spaces = 24 - len(key)  
          spaces = " " * num_spaces
          print(f"{i} | {key}{spaces} | ${value}")
          menu_items[i] = {
            "Item name": key,
            "Price": value  
          }
          i += 1
# 2. Ask customer to input menu item number
      item_number = input("Enter item number: ")
     # 3. Check if the customer typed a number
      if item_number.isdigit():
        # Convert the menu selection to an integer
        item_number = int(item_number)
      # 4. Check if the menu selection is in the menu items
        if item_number in menu_items:
          # Store the item name as a variable
          item_name = menu_items[item_number]["Item name"] 
          # Ask the customer for the quantity of the menu item
          quantity = input(f'How many {item_name}s would you like? (default is 1): ')
           # Check if the quantity is a number, default to 1 if not
          if not quantity.isdigit():
            quantity = 1
          else:
            quantity = int(quantity)
            # Add the item name, price, and quantity to the order list
          order_list.append({
            'Item name': item_name,
            'Price': menu_items[item_number]["Price"],
            'Quantity': quantity
          })

            # Tell the customer that their input isn't valid
            # Tell the customer they didn't select a menu option

# Ask the customer if they would like to order anything else
 # 5. Check the customer's input
  response = input("Would you like to continue ordering? (yes/no): ").lower()
  if response == 'no':
    place_order = False
    print("Thank you for your order!")
     # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again

# Print order receipt 
# Print out the customer's order 
print("\nOrder Receipt:")

# Uncomment the following line to check the structure of the order
#print(order)
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
# 6. Loop through the items in the customer's order
# 7. Store the dictionary items as variables
for item in order_list:
  item_name = item["Item name"]
  price = item["Price"]
  quantity = item["Quantity"]
# 8. Calculate the number of spaces for formatted printing
  spaces_name = " " * (30 - len(item_name))
  spaces_price = " " * (8 - len(str(price)))
  spaces_quantity = " " * (10 - len(str(quantity)))
 # 9. Create space strings


    # 10. Print the item name, price, and quantity
  print(f"{item_name}{spaces_name} | ${price}{spaces_price} | {quantity}{spaces_quantity}")
 # 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_price = sum(item["Price"] * item["Quantity"] for item in order_list)  
print(f"\nTotal Price: ${total_price:.2f}")
