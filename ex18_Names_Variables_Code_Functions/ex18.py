# This one is like your scripts from argv.
def print_two(*args):  # Ok, I lied...
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

# Ok, that *args is pointless, we can just do this..


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument.


def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments.


def print_none():
    print("I have none.")


print_two("Andy", "Thomas", "Young")
print_two_again("Andy", "Young")
print_one("First!")
print_none()
