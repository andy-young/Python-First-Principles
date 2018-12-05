# Implicit actions of defining a function on parent but not child

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# The use of pass under the class Child: is how you tell Python that you want
# an empty block. This creates a class named Child but says that there's nothing
# new to define in it. Instead it will inherit all of its behavior from Parent.

# Even though I'm calling son.implicit() on line 15, while Child does not have
# an implicit function defined, it still works, and calls the one defined on
# Parent. This shows that if we put functions in a base class (i.e. Parent)
# then all subclasses (i.e. Child) will automatically get those features.