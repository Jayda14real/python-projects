import random
def escape_game():
    print("Welcome to the Escape Game!")
    print("Your task is to pick the correct option to live, pick the wrong one and you die.")
    input("You have 3 doors to chose from, door 1, door 2 and door 3. Which door do you choose?")

    outcome = ["You chose the correct door and you move on to the next area!", "You fall into a pit of poisonous snakes, game over.", "You get eaten by a pack of hungry lions, game over."]
    result = random.choice(outcome)
    if result == "You chose the correct door and you move on to the next area!":
        print("Congrats! You chose the right choice, now you have to find a way across the river.")
    elif result == "You fall into a pit of poisonous snakes, game over.":
        print("you fall into a pit of poisonous snakes, game over,")
    elif result == "You get eaten by a pack of hungry lions, game over.":
        print("You get eaten by a pack of hungry lions, game over")

    input2 = input ("Do you choose to swim across the river or wait for a boat?")
    if input2 == "Swim across the river":
        print("You got eaten by a shark in the river, game over.")
    elif input2 == "Wait for the boat":
        print("You wait for the boat and the boat crashes, but you survive.")





    # outcome2 = ["You get eaten by a shark in the river, game over.", "The boat crashes but you survive."]
    # if input == "swim":
    #     print("You get eaten by a shark in the river, game over.")
    # else:
    #     print("you wait for the boat but the boat crashes and you survive.")

escape_game()