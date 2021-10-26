# Homework to make a choose you own adventure similar to ex35. Draw it out then create the adventure. Add monsters, traps, doors, description.

from sys import exit

def dead(message):
    print(message)
    exit(0)

def portal():
    print("There's a giant demon, what shall you do?")
    print("Use lightsaber, cry, run away")

    choice = input("> ")

    if choice == "Use lightsaber":
        dead("ZIPZAP ZOOP SCOOP, the demon is ded. You accidently zip zap zoop scoop yaself tho, you're dead.")
    elif choice == "cry":
        dead("You cry like a little bitch and the demon eats ya. You ded.")
    elif choice == "run away":
        dead("You trip and fall and die. The demon then eats ya body.")


def main():
    print("You wake up in the morning feelin' like p-diddy")
    print("There are glasses, a toothbrush, and a door.")
    print("What do you do?")

    while True:
        choice = input("> ")

        if choice == "grab glasses":
            print("You grab your glasses");
        elif choice == "brush teeth":
            print("Before you leave you brush you teeth with a bottle of jack.")
        elif choice == "open door":
            print("You open the door and dash out, you're gunna hit this city (let's go).")
            portal()
        else:
            print("Tick-tock, on the clock. That's not a choice.")

main()