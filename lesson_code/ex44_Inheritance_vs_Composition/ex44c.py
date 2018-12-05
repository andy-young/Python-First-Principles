# ALTER BEFORE OR AFTER
# =============================================================================

# The third way to use inheritance is a special case of overriding where you
# want to alter the behavior before or after the Parent class's version runs.
# We first override the function Explicitly, but then we use a Python built-in
# function named 'super' to get the Parent version to call.

class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()              # calls the Parent version..
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()


# 1. We overridden Parent.altered (line 17), now the Child.altered version runs
# 2. Line 19 we call Parent.altered() with 'super'

# 3. Line 19 super(Child, self).altered() is aware of inheritance and will get
#    the Parent class for us. Reads as "call super with arguments Child and
#    self, then call the function altered on whatever it returns."

# 4. Now the Parent.altered version of the fxn runs, and prints out line 12
# 5. Lastly, execution returns to Child.altered() and line 20 executes a print()