# We will make strings with variables imbedded in them.

my_name = "Andy Young"
my_age = 38
my_height = 66  # inches
my_weight = 160 # pounds
my_eyes = "green"
my_teeth = "white"
my_hair = "brown"

# The 'f' before the string tells python to 'format' the string.
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")