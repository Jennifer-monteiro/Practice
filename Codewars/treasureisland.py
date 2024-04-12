print("Welcome to treasure island game")
print("Your mission is to find treasure")

user = input("Pick a movement: ")
if user == "left":
    print("Keep Going")
    user = input("Swim or Wait: ")
    if user == "swim":
        print("Game over")
    elif user == "wait":
        print("Keep Going")
        user = input("Which door? red, blue or yellow: ")
        if user == "red":
            print("Game over")
        elif user == "blue":
            print("Game over")
        elif user == "yellow":
            print("You win")
        else:
            print("Invalid Input")
elif user == "right":
    print("End Game")
else:
    print("Invalid Input")
