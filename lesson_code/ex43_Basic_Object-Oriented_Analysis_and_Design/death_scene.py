class Death(object):

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