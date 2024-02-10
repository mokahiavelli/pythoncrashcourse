while True:
    topping = input("Enter a pizza topping (or 'quit' to exit): ")
    
    if topping.lower() == 'quit':
        print("Finished adding all pizza toppings.")
        break
    
    print(f"Adding {topping} to your pizza.")
