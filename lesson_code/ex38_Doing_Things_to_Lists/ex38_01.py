# Create a space separated string of 2 words called 'six_things'

six_things = "Computer Capsule"

objects = six_things.split(None) # ["Computer", "Capsule"]
print("'six_things' was split and assigned to 'objects'.\n")

print(f"\tObjects -> {objects}\n")

desk_items = ["Mouse", "Keyboard", "Cords", "Lamp", "Mic", "Camera"]

while len(objects) != 8:
    a_desk_item = desk_items.pop()
    print(f"Appending: {a_desk_item} to {objects}\n")
    objects.append(a_desk_item)
    print(f"There are {len(objects)} objects now.\n")
    print(f"And 'desk_items' are being removed! -> {desk_items}\n")


print(f"Let's see objects increasing: {objects}\n")

print("Let's take some objects.\n")

print(f"The second item is the list is {objects[1]}.\n")
print(f"The second to last item is {objects[-2]}\n")
print(f"The last object is {objects.pop()}.\n")
print(f"Smileys in between objects -> {'--'.join(objects[2:6])}\n")
