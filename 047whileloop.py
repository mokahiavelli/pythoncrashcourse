while True:
    age_input = input("Welcome to Brian's Cinema, how old are you? (Type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break

    age = int(age_input)

    if age < 3:
        print("Your entrance incurs no fee :)")
    elif age < 13:
        print("Your ticket will be ten bucks please!")
    elif age > 12:
        print("Your ticket will be fifteen bucks please!")
