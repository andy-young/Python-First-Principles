class EscapePod(scene):

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

