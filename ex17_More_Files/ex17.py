# Import the argv array of CLI arguments from the sys module.
from sys import argv

# Import exists method from os.path module.
# exist returns a Boolean if the file exists.
from os.path import exists

# argv unpacks its arguments.
script, from_file, to_file = argv

# Print the names of the from_file & to_file.
print(f"Copying from {from_file} to {to_file}.")

# open(file) returns corresponding file obj to in_file variable.
# in_file is redundant, could be -> indata = open(from_file).read().
in_file = open(from_file)

# Read the contents of in_file and assign to indata.
# .read(n) takes an integer argument and outputs n characters (bytes).
indata = in_file.read()

# len() returns the number of items in the object being called on.
# Print the number of characters in the (byte) string.
print(f"The input file {len(indata)} bytes long.")

# Print True or False if the file is in the path.
print(f"Does the output file exist? {exists(to_file)}")

# Compel User to make and/or write to file or not.
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Open to_file, and give it write access, then assign it to out_file.
out_file = open(to_file, 'w')

# Write the contents of indata to out_file.
out_file.write(indata)

# Tell user process is complete.
# If to_file exists, then the contents of from_file will
# be written to it.
# When a to_file is passed to ex17.py that does not exist,
# it will be created and given the contents of from_file.
print("Alright, all done.")

# Close both files.
out_file.close()
in_file.close()
