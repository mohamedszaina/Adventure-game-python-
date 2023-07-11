import time
import random


def print_delay(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def introduction(choice):
    print_delay("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_delay(f"Rumor has it that a {choice} is somewhere around "
                "here and has been terrifying the nearby village.")
    print_delay("In front of you is a house.")
    print_delay("To your right is a dark cave.")
    print_delay("In your hand, you hold your trusty (but not very "
                "effective) dagger.")


def cave(object, choice):
    if "sword" in object:
        print_delay("You peer cautiously into the cave.")
        print_delay("You've been here before, and you've collected all "
                    "the good stuff. It's just an empty cave now.")
    else:
        print_delay("You peer cautiously into the cave.")
        print_delay("It turns out to be only a very small cave.")
        print_delay("Your eye catches a glint of metal behind a rock.")
        print_delay("You have found the magical Sword of Ogoroth!")
        print_delay("You discard your silly old dagger and take "
                    "the sword with you.")
        object.append("sword")
    print_delay("You walk back out to the field.")
    field(object, choice)


def house(object, choice):
    print_delay("You approach the door of the house.")
    print_delay(
        f"You are about to knock when the door opens and out steps a {choice}.")
    print_delay(f"Eep! This is the {choice}'s house!")
    print_delay(f"The {choice} attacks you!")
    if "sword" not in object:
        print_delay("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) run away?")
        if choice2 == "1":
            if "sword" in object:
                print_delay(
                    f"As the {choice} moves to attack, you unsheath your new sword.")
                print_delay("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the attack.")
                print_delay(f"But the {choice} takes one look at "
                            "your shiny new toy and runs away!")
                print_delay(
                    f"You have rid the town of the {choice}. You are victorious!")
            else:
                print_delay("You do your best...")
                print_delay(f"but your dagger is no match for the {choice}.")
                print_delay("You have been defeated!")
            play_again()
            break
        elif choice2 == "2":
            print_delay(
                "You run back into the field. Luckily, you don't seem to have been followed.")
            field(object, choice)
            break


def field(object, choice):
    print_delay("Enter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")
    while True:
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            house(object, choice)
            break
        elif choice1 == "2":
            cave(object, choice)
            break


def play_again():
    while True:
        again = input("Would you like to play again? (y/n)").lower()
        if again == "y":
            print_delay("\n\n\nExcellent! Restarting the game ...\n\n\n")
            play_game()
            break
        elif again == "n":
            print_delay("\n\n\nThanks for playing! See you next time.\n\n\n")
            break


def play_game():
    object = []
    choices = ["wicked fairie", "pirate", "dragon", "troll", "gorgon"]
    choice = random.choice(choices)
    introduction(object, choice)
    field(object, choice)


play_game()
