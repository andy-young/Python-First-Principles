class Scene(object):

  def enter(self):
    print("This scene is not yet configured.")
    print("Subclass it and implement enter().")
    exit(1)

# This is just a demo of what all the base class 'Scene' will be
# able to do. That is to say, all instances of Scene will have a 'enter' function.