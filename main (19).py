def escape_game():
    print("Welcome to the Escape Game.")
    print("Your mission is to escape a dangerous area.")

#First decision
choice1 = input("Do you go left or right?").lower()
if choice1 != "left":
    print("You fall into a graveyard. Game Over.")

#Second decision
choice2 = input("Do you swim or wait?").lower()
if choice2 != "wait":
    print("You are attacked by a shark. Game Over.")

#Third decision
choice3 = input("Which door? (Yellow, Red, or Orange):").lower()
if choice3 == "yellow":
    print("You are burned by a dragon. Game Over.")

elif choice3 == "red":
    print("You are eaten by a lion. Game Over.")

elif choice3 == "orange":
    print("Congratulations! You Win!")

else:
    print("Game Over.")

#Run the Game
escape_game()
#still a work in progress, need to work out a few things













