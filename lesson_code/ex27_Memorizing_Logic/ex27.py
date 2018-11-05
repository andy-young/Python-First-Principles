# Memorizing Truth Tables
# ==============================

# Write out the Truth Terms:

# => and
# => or
# => not
# => != (not equal) Write this with an exclamation point followed my an equals sign.
# => == (equal)
# => >= (greater-than-equal)
# => <= (less-than-equal)
# => True
# => False


print("The 'NOT' operator:")
print("\tnot True => ", not True)    # => False
print("\tnot False => ", not False)  # => True

print("\nThe 'OR' operator:")
print("\tTrue or False => ", True or False)    # => True
print("\tTrue or True => ", True or True)      # => True
print("\tFalse or True => ", False or True)    # => True
print("\tFalse or False => ", False or False)  # => False

print("\nThe 'AND' operator:")
print("\tTrue and False => ", True and False)    # => False
print("\tTrue and True => ", True and True)      # => True
print("\tFalse and True => ", False and True)    # => False
print("\tFalse and False => ", False and False)  # => False

print("\nLet's combine 'NOT OR':")
print("\tnot(True or False) => ", not(True or False))   # => False
print("\tnot(True or True) => ", not (True or True))    # => False
print("\tnot(False or True) => ", not (False or True))  # => False
print("\tnot(False or False) => ", not(False or False)) # => True

print("\nLet's combine 'NOT AND':")
print("\tnot(True and False) => ", not(True and False))   # => True
print("\tnot(True and True) => ", not (True and True))    # => False
print("\tnot(False and True) => ", not (False and True))  # => True
print("\tnot(False and False) => ", not(False and False)) # => True

print("\nThe 'not equals' operator (!=):")
print("\t1 != 0 => ", 1 != 0)  # => True
print("\t1 != 1 => ", 1 != 1)  # => False
print("\t0 != 1 => ", 0 != 1)  # => True
print("\t0 != 0 => ", 0 != 0)  # => False

print("\nThe '==' (equals) operator:")
print("\t1 == 0 => ", 1 == 0)  # => False
print("\t1 == 1 => ", 1 == 1)  # => True
print("\t0 == 1 => ", 0 == 1)  # => False
print("\t0 == 0 => ", 0 == 0)  # => True