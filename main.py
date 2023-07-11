import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(option):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {option} is somewhere around "
                "here and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold your trusty (but not very "
                "effective) dagger.")


def cave(item, option):
    if "sword" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and you've collected all "
                    "the good stuff. It's just an empty cave now.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        item.append("sword")
    print_pause("You walk back out to the field.")
    field(item, option)


def house(item, option):
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens and out steps a {option}.")
    print_pause(f"Eep! This is the {option}'s house!")
    print_pause(f"The {option} attacks you!")
    if "sword" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) run away?")
        if choice2 == "1":
            if "sword" in item:
                print_pause(
                    f"As the {option} moves to attack, you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the attack.")
                print_pause(f"But the {option} takes one look at "
                            "your shiny new toy and runs away!")
                print_pause(
                    f"You have rid the town of the {option}. You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause(f"but your dagger is no match for the {option}.")
                print_pause("You have been defeated!")
            play_again()
            break
        elif choice2 == "2":
            print_pause(
                "You run back into the field. Luckily, you don't seem to have been followed.")
            field(item, option)
            break


def field(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    while True:
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break


def play_again():
    while True:
        again = input("Would you like to play again? (y/n)").lower()
        if again == "y":
            print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
            play_game()
            break
        elif again == "n":
            print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
            break


def play_game():
    item = []
    options = ["wicked fairie", "pirate", "dragon", "troll", "gorgon"]
    option = random.choice(options)
    intro(item, option)
    field(item, option)


play_game()