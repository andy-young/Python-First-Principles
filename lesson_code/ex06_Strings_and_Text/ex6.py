# Set the integer 10 to the variable 'types_of_people'.
types_of_people = 10

# Format the string with the interpolated variable 'types_of_people' and assign it to 'x'.
x = f"There are {types_of_people} types of people."

# Set the string 'binary' to var binary, etc.
binary = "binary"
do_not = "don't"

# Repeat the same pattern with y as we did with variable x on line 4.
y = f"Those who know {binary} and those who {do_not}."

# Print the output of both x & y variables.
print(x)
print(y)

# Now interpolate variables x & y into a string and print.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set the Boolean False to 'hilarious'.
hilarious = False

# Set a string with an empty curly brace to a variable.
joke_evaluation = "Isn't that joke so funny?! {}"

# Format the joke_evaluation string with the hilarious variable as an argument, and print.
print(joke_evaluation.format(hilarious))

# Set to strings to two more variables.
w = "This is the left side of..."
e = "a string with a right side."

# Concatonate the w variable with the e variable and print.
print(w + e)