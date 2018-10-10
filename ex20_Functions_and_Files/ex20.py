# get argv from sys module
from sys import argv

# have argv unpack to argument variables
script, input_file = argv


# fxn takes an open(ed) file as arg & reads it and prints
def print_all(f):
    print(f.read())


# seek(0) moves to 0 byte (first byte) in the file
def rewind(f):
    f.seek(0)


# readline() reads one line from the file, that line gets concatenated
# with the line_count argument which in our case is an integer.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# end functions ===============================================================

# open file and assign
current_file = open(input_file)

print("First, let's print the entire file:\n")

# calls read() on argument
print_all(current_file)

print("Let's rewind, like a tape.")

# rewind just calls .seek(0) on the file
rewind(current_file)

print("Let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)
# >>> 1 This is line 1

current_line += 1
print_a_line(current_line, current_file)
# >>> 2 This is line 2

current_line += 1
# >>> 3 This is line 3
print_a_line(current_line, current_file)
