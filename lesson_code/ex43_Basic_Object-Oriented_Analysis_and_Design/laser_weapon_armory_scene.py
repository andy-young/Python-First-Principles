class LaserWeaponArmory(scene):

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