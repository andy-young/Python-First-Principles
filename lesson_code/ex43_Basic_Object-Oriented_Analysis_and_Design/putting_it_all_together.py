# Step 1: add all the modules you will need for the game
from sys import exit
from random import randint
from textwrap import dedent

# Step 2: Add your Scene Object
class Scene(object):

  def enter(self):
    print("This scene is not yet configured.")
    print("Subclass it and implement enter().")
    exit(1)

# Step 3: Add Engine Object
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

# Step 4: Add all six Scenes
class Death(Scene):

  quips = [
    "A floor panel before you suddenly shifts open and you feel yourself being pulled into a bone shattering abyss.",
    "Noxious vapors choke your eyes and seize you throat as your conscienceness fades to black.",
    "A crack in the hull rapidly pulls you into the vacuum of space.",
    "You suddenly lose feeling in from your neck down as your cervical column is severed.",
    "An auto sentry harpoons you through the neck."
  ]

  def enter(self):
    print(Death.quips[randint(0, len(self.quips) - 1)])
    exit(1)

class CentralCorridor(Scene):

  def enter(self):
    print(dedent("""
      An ominous force has inhabited your ship and there is no trace of your crew.
      You seem to be the last surviving member and in such situations you are have
      been instructed and trained to detonate the ship as your first priority,
      survival is secondary. There is an anti-matter bomb in the Weapons Armory,
      put it in the Bridge, and set the detonation sequence while you attempt escape.

      You're running down the central corridor to the Weapons Armory when an amorphous
      inky black entity appears two arm lengths in front of you. It's blocking the door
      to the Armory and reaching towards your eyes.
    """))

    action = input("> ")

    if action == "shoot!":
      print(dedent("""
        Quick on the draw you yank out your personal weapon and fire into the cloud.
        It only flows around the projectile, harming nothing as it envelopes your body
        it sering agony as your conscienceness fades.
      """))

      return 'death'

    elif action == 'dodge':
      print(dedent("""
        You dodge, weave and slip-slide right as the form's cold embrace tickles the small of
        your back. You feel euphoria and wake up with your conscienceness seemingly contained
        for eternity in dark sleeping paralysis.
      """))

      return 'death'

    elif action == 'focus mind':
      print(dedent("""
        You close your eyes against all survival instincts and feel the warm embrace of water
        cascade around your body. In shock at such a peculiar event, you open your eyes and see your
        path to the Armory clear.
      """))

      return 'laser_weapon_armory'

    else:
      print("Try this again..")
      return 'central_corridor'

class EscapePod(Scene):

  def enter(self):
    print(dedent("""
      You make it to the pods. There are five remaining, perhaps disabled, which one
      do you choose?
    """))

    good_pod = randint(1, 5)
    guess = input("[pod #]> ")


    if int(guess) != good_pod:
      print(dedent("""
        You jump into pod {guess} and hit eject. The pod implodes as you are crushed instantly.
      """ ))
      return 'death'

    else:
      print(dedent("""
        You jump into pod {guess} and hit the eject button. As you drift into space you see the explosion
        and know that you have survived.
      """))

      return 'finished'

class LaserWeaponArmory(Scene):

  def enter(self):
    print(dedent("""
      You enter the weapons armory with an ominous feeling. In the far side of the room
      you see the anti-matter bomb in a locked container. There's a keypad lock containing
      the device and you have only ten attempts to get it right. The code is 3 digits.
    """))

    code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
    guess = input("[keypad]> ")
    guesses = 0

    while guess != code and guesses < 10:
      print("Error, wrong code.")
      guesses += 1
      guess = input("[keypad]> ")

    if guess == code:
      print(dedent("""
        The container clicks open and the seal breaks, letting out gas. You take it to the bridge
        and place it in the designated area.
      """))
      return 'the_bridge'

    else:
      print(dedent("""
        The lock buzzes one last time and then you hear the device fuze shut forever.
        The evil force seeps in from every corner and you resign yourself to what horrors unfold.
      """))
      return 'death'

class TheBridge(Scene):

  def enter(self):
    print(dedent("""
      You burst into the Bridge with the anti-matter bomb and several dark forms are
      situated around the bridge as if waiting for you.
    """))

    action = input("> ")

    if action == "throw the bomb":
      print(dedent("""
        In a panic you throw the bomb and all hope is lost, because you are instantly
        killed by the explosion.
      """))
      return 'death'

    elif action == "slowly place the bomb":
      print(dedent("""
        You place the bomb on the floor and the forms hold their position. You run to the escape pods.
      """))

      return 'escape_pod'

    else:
      print("Try again.")
      return "the_bridge"

class Finished(Scene):

    def enter(self):
        print("You won! Good Job.")
        return 'finished'

# Step 5: Add The Map Object
class Map(object):

    scenes = {
      'central_corridor': CentralCorridor(),
      'laser_weapon_armory': LaserWeaponArmory(),
      'the_bridge': TheBridge(),
      'escape_pod': EscapePod(),
      'death': Death(),
      'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
      val = Map.scenes.get(scene_name)
      return val

    def opening_scene(self):
      return self.next_scene(self.start_scene)

# Lastly, add the code to make the program run
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()