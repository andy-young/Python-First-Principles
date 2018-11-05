# end= ' ' tells print to not end the line with a newline char and go to the next line.
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# What you should see (If you're me):
# How old are you? 38
# How tall are you? 66"
# How much do you weigh? 150lbs
# So, you're 38 old, 66" tall and 150lbs heavy.

# =============================================
# To take a number input and convert from string to integer
# use a variable like this: x = int(input())
# the int method will convert to integer so you may do math on it.