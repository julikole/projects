import time
import random
import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


sound_effects = ["bam! BOOM!", "schoiiiiing!", "BIFF! BAM! POW!",
                 "klink-klonk", "boiiiiink!"]
villain_list = ["monster", "troll", "witch", "cyclop", "werewolf"]
villain = random.choice(villain_list)


def print_pause(message, sleep_time=2):
    print(Color.get_color() + message)
    time.sleep(sleep_time)


def valid_input(message, options):
    while True:
        option = input(message).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. '
                    'Please try again!')


def intro():

    print_pause("You find yourself in a middle of an open field, "
                "surrounded by colorful flowers and tall grass.")
    print_pause(f"Rumor has is it that a scary {villain} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a dungeon.")
    print_pause("To your right is a dark cave.", sleep_time=3)
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")
    print_pause("What would you like to do?")


def cave(weapons):
    print_pause("You peer into the dark endless cave.")

    if "sword" in weapons:
        print_pause("There is nothing more here.")
    else:
        print_pause("You see a magic sword in the corner, "
                    "and you rush towards it to pick it up.")
        print_pause("You discard your old dagger and pick up "
                    "the sword.")
        weapons.append("sword")

    print_pause("You walk back to the field.")

    in_field(weapons)


def dungeon(weapons):
    print_pause("You approach the dungeon, and walk slowly inside.", 3)
    print_pause("You hear steps approaching you.", 3.5)
    print_pause(f"All of a sudden, a vicious {villain} "
                "steps out and starts attacking you.")
    print_pause(f"Would you be able to defeat the {villain} and "
                "put an end to the villagers' nightmare?")

    fight(weapons)


def fight(weapons):

    choice_options = f"Enter 1 to fight the {villain}\n" \
                      "Enter 2 to run away\n"

    choice = valid_input(choice_options, ['1', '2'])

    if "1" in choice:
        if "sword" in weapons:
            print_pause(random.choice(sound_effects), 2)
            for i in range(5):
                print_pause(random.choice(sound_effects), 1-0.2*i)
            print_pause(f"The {villain} falls over.")
            print_pause("Congratulations! You won!")
        else:
            print_pause(random.choice(sound_effects))
            print_pause(f"Your tiny dagger is no match for the {villain}!")
            print_pause("You have been defeated!")
            print_pause("GAME OVER")
        game_end()
    elif "2" in choice:
        print_pause("You are back in the field.")
        print_pause("What would you like to do now?")
        in_field(weapons)


def in_field(weapons):
    choice_options = "Enter 1 to enter the dungeon\n" \
                     "Enter 2 to peer into the cave\n"
    location = valid_input(choice_options, ['1', '2'])
    if location == "1":
        dungeon(weapons)
    elif location == "2":
        cave(weapons)


def game_end():
    question = "Would you like to play again? (y/n)"
    play_again = valid_input(question, ['y', 'n'])
    if play_again == "y":
        print_pause("Excellent! Let's start!")
        start_game()
    elif play_again == "n":
        print_pause("Alrighty, bye bye!")


def start_game():
    weapons = []
    global villain
    villain = random.choice(villain_list)
    intro()
    in_field(weapons)


start_game()
