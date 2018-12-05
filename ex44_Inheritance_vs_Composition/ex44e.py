# COMPOSITION
# =============================================================================

# Inheritance is useful, but another way to do the exact same thing is just to
# use other classes and modules, rather than rely on implicit inheritance.


class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()


# There is no parent-child (is-a) relationship. There's a 'has-a' relationship.
# Where Child 'has-a' Other that is uses to get its work done.
