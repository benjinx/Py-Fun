# Name: Gothons from Planet Percal #25

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    def enter(self):
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        You wake up, rub your eyes, you look around you.
        You see a gothon standing there MENACINGLY.
        "AYE BOI-O! YOU BETTER BE FAST OR YOU'RE DEAD" he screams\n
        """))
        print("What do you do?\n")
        print("Tell joke")
        print("Fight")
        print("Flee")

        action = input("> ")

        jokeList = ["Which bear is the most condescending? A pan-duh!",
                    "What kind of noise does a witch’s vehicle make? Brrrroooom, brrroooom.",
                    "What’s brown and sticky? A stick.",
                    "Two guys walked into a bar. The third guy ducked.",
                    "How do you get a country girl’s attention? A tractor.",
                    "Why are elevator jokes so classic and good? They work on many levels.",
                    "What do you call a pudgy psychic? A four-chin teller.",
                    "What did the police officer say to his belly-button? You’re under a vest.",
                    "What do you call it when a group of apes starts a company? Monkey business.",
                    "My wife asked me to stop singing “Wonderwall” to her. I said maybe…"]

        if (action == "Tell joke" or action == "tell joke" or action == "Tell Joke"):
            print(jokeList[randint(0, len(jokeList) - 1)])
            print("The gothon sighs heavily and moves out of the way of the door behind him. 'Just fucking go!' he says while pointing at the door way.")
            return 'laser_weapon_armory'
        elif (action == "Fight" or action == "fight"):
            print("You swing a mean right hook at the gothon. He grabs your face and super slams it into the ground. You're dead. Good job kid.")
            return 'death'
        elif (action == "Flee" or action == "flee"):
            print("You turn to run away, you trip and fall. The gothon eats you. F.")
            return 'death'
        else:
            print("??? that aint real")
            return 'central_corridor'


# Laser Weapon Armory - This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You dive roll into the Weapon Armory, crouch and scan the room for more Gothons that could be lurking ANYWHERE!
        It's quiet... Too quiet...
        You hear a gothon fart from down the hall behind you where you came in.
        You turn and look as he scratches his ass.
        You continue down the hallway away from him.
        Careful to not draw attention to yourself and low and behold there it is!
        It's the neutron bomb in it's container.
        There's a keypad lock on the box and you need the code to get the bomb out.
        You notice it's 3 digits.
        There's a sticky note on the lock. You take it and read it. 
        'If you get the code wrong 10 times AGAIN..... Jerry...... the keypad will disable AGAIN...
        until IT gets around to fixing it, you know how long that took last time.'
        """))
        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDDD!")
            guesses += 1

            # Cheater cheater
            if guess == "cheat" or guess == "cheatcode":
                print("Congrats you cheated. You're a piece of shit. Good job. Here's the code:")
                print(code)

                # if you cheat why should this count as a guess eh?
                if guesses > 0:
                    guesses -= 1

            guess = input("[keypad]> ")



        if guess == code:
            print(dedent("""
                *Click* The container clicks open and the seal breaks, LETTING GAS OUT!
                You grab the neutron bomb and run as fast as you can to the bridge where you
                need to place it to blow this whole place.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time... and then you hear a sickening melting
                sound as the mechanism is fused together.
                You sit there staring at it. A gothon puts his hand on your shoulder.
                You look at him and his name tag. 'Jerry'.
                "Oh fucking great what the hell am I going to do NOW!?"
                "They're going to be PISSED AND THINK I DID THIS!"
                Jerry grabs you and rips you in half. Munching on your brains after because why not.
            """))
            return 'death'

# The Bridge - This is another battle scene with a Gothon where the hero places the bomb.
class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the neutron destruct bomb
        under your arm and surprise 5 Gothons who are trying to
        take control of their lives. Each of them have an even uglier
        clow costume on than the last. They haven't pulled their weapons
        out yet, as they see the ative bomb under your arm and don't
        want to set it off.
        """))
        print("What do you do?\n")
        print("Throw bomb")
        print("Place bomb")

        action = input("> ")

        if action == "Throw bomb" or action == "throw bomb" or action == "Throw Bomb":
            print(dedent("""
            In a panic you YEEEEEEET the bomb at the group of Gothons and make a leap for the door.
            Right as you drop it a Gothon shoots you right in yo back. You look up and see the Gothon
            disarm the bomb right as you lose consciousness, GG. You died, and you failed the mission.
            """))
            return 'death'
        elif action == "Place bomb" or action == "place bomb" or action == "Place Bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and the Gothons put their hands up
            and start to sweat. You inch backward to the door, open it, and then carefully place
            the bomb on the floor, pointing your blaster at it. You then jump back through the door,
            punch the close button and BLAST the lock so the Gothons can't get out.
            Now that the bomb is placed you run to the escape pod to get off this tin can.
            """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE. BRRRRRRRRRRRRRRRRRRRRRRR")
            return 'the_bridge'

# Escape Pod - This is where the hero escapes but only after guessing the right escape pod.
class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through the doors of the escape pod room trying to make it to an escape pod
        before the whole ship explodes. It seems like not many of the Gothons are chasing you.
        You look before you and see 5 escape pods. They all seem in rough shape, which do you take?
        You only have one chance.
        """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")
        
        if guess == "cheat" or guess == "cheatcode":
            print("Congrats you cheated. You're a piece of shit. Good job.")
            print("The only pod that works has a bright green aura glowing around it now.")
            print(good_pod)
            print(dedent(f"""
            You see the bright green glowing aura around the CHEATERS pod {guess} and you jump in.
            You hit the eject button. The pod shoots out into space, smooth as butter. PLOOP.
            It's headed towards the closest planet. As it flies to the planet, you look back and
            your ship implode then explode like a bright star, taking with it the Gothon ship at the same time.
            ... You did it... those bastards are finally dead and you've escaped. Congratulations. You
            won the game... cheater...
            """))
            return 'finished'
        elif int(guess) != good_pod:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button. The pod escapes out into the void of space, then...
            it starts to rumble. Somethings not right... BOOM! the whole escape pod implodes as the hull ruptures,
            crushing your body into jam jelly. Grape flavored too.
            """))
            return 'death'
        else:
            print(dedent(f"""
            You jump in pod {guess}. You hit the eject button. The pod shoots out into space, smooth as butter. PLOOP.
            It's headed towards the closest planet. As it flies to the planet, you look back and
            your ship implode then explode like a bright star, taking with it the Gothon ship at the same time.
            ... You did it... those bastards are finally dead and you've escaped. Congratulations. You
            won the game.
            """))
            return 'finished'

# Finished
class Finished(Scene):

    def enter(self):
        print("You did it! YAY!")
        exit(0)

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
