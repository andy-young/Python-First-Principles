# OVERRIDE EXPLICITLY
# =============================================================================

# The problem with having functions called implicitly is sometimes you want
# the child to behave differently.
# In this case we want to override the function in the child, thereby replacing
# the functionality. To do this, just define a function with the same name
# in Child..

class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()


# Child overrides the function by defining its own version --> line 15