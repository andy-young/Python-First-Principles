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