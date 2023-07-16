import time
import random


def print_pause(*messages):
    for message in messages:
        print(message)
        time.sleep(2)


def intro():
    print_pause(
        "You find yourself standing in an open field, filled with grass "
        "and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a wicked fairy is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand, you hold your trusty (but not very effective) "
        "dagger."
    )


def get_choice():
    choice = input(
        "What would you like to do?\n"
        "1. Knock on the door of the house.\n"
        "2. Peer into the cave.\n"
        "Please enter 1 or 2.\n"
    )
    while choice != "1" and choice != "2":
        choice = input("Please enter 1 or 2.\n")
    return choice


def fight(enemy):
    print_pause("You decide to stand your ground and fight!")
    if random.randint(0, 1) == 0:
        print_pause(f"You defeat the {enemy} in a fierce battle!")
        print_pause("Congratulations! You win!")
    else:
        print_pause(f"Oh no! The {enemy} overpowers you.")
        print_pause("Game over.")


def cave():
    print_pause("You peer cautiously into the cave.")
    if random.randint(0, 1) == 0:
        print_pause("You enter the cave and discover a treasure chest!")
        reward = random.choice(["magic potion", "gold coins",
                                "ancient artifact"])
        print_pause(f"You found a {reward}! Congratulations!")
        print_pause("You win!")
    else:
        enemyList = ["vicious troll", "ferocious dragon", "cunning goblin"]
        enemy = random.choice(enemyList)
        print_pause(f"You enter the cave and encounter a {enemy}.")
        print_pause(f"The {enemy} attacks you!")
        fight(enemy)


def field():
    print_pause("You run back to the field.")
    # Additional random event in the field
    if random.randint(0, 1) == 0:
        print_pause("You stumble upon a hidden path.")
        print_pause("Do you want to explore it?")
        explore_choice = input("Enter 'y' for yes or 'n' for no.\n").lower()
        if explore_choice == "y":
            print_pause("You follow the path and find a secret treasure!")
            print_pause("Congratulations! You win!")
        else:
            print_pause("You decide not to explore the hidden path.")
            print_pause("You continue your adventure.")


def house():
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps"
        " a wicked fairy."
    )
    print_pause("Eep! This is the wicked fairy's house!")
    print_pause("The wicked fairy attacks you!")
    fight("wicked fairy")


def play_game():
    intro()
    choice = get_choice()
    if choice == "1":
        house()
    else:
        cave()
    play_again()


def play_again():
    choice = input("Would you like to play again? (y/n)\n").lower()
    while choice != "y" and choice != "n":
        choice = input("Please enter 'y' or 'n'.\n").lower()
    if choice == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    else:
        print_pause("\n\n\nThanks for playing! Goodbye!")


play_game()
