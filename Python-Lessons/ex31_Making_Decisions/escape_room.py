print("""You're in a Room.\n
You can see a 'Mirror', a 'Desk', a 'Fridge' and a 'Door'.\n
\tWhich should you inspect?""")

roomNode = input("> ").lower()

if roomNode == "mirror":
    print("The Mirror is cracked slightly. You can see something behind it.")
    print("What should you do?")
    print("\tSee 'behind Mirror'?")
    print("\tLook at your 'reflexion'.")
    print("\t'Avoid' the mirror.")

    mirror_node = input("> ").lower()


#  ===========================Start roomNode ==================================

if roomNode == "desk":
    print("You notice three draws, left, middle, and right side.")
    print("Should you inspect the drawers? Yes or No?")

    drawNode = input("> ").lower()

    if drawNode == 'yes':
        print("Which draw would you like to open?")
