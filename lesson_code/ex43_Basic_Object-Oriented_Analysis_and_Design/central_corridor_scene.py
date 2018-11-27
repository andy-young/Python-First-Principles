class CentralCorrridor(Scene):

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