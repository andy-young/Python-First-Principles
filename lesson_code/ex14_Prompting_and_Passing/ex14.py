from sys import argv
# from the sys module suite -> import argv module

script, user_name, timeStamp = argv
prompt = '> '

print(f"The current time is: {timeStamp}.")
print(f"Hi {user_name}, I'm the {script}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Now the time is {int(timeStamp) + 0.01}
""")
