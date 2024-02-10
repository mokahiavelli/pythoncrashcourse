age = int(input("Welcome to Brian's Cinema, how old are you?: "))

if age < 3:
    print("Your entrance incurs no fee :)")
elif age < 13:
    print("Your ticket will be ten bucks please!")
elif age > 12:
    print("Your ticket will be fifteen bucks please!")