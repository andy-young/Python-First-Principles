# Convert this while-loop to a function that you can call, and replace 6 in
# the test (i < 6) with a variable.

i = 0
numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"A the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)

def fill_array_with_numbers(iterator, increment_Num, limit):
  numbers = []

  if iterator >= limit:
    print(f"Your iterator ({iterator}) can't exceed your limit ({limit}).")
    print("\tOtherwise the loop won't fail.\n")
    return
  elif iterator < 1:
    print("Your iterator must be greater than 0.\n")
    return

  while iterator < limit:
      numbers.append(iterator)
      print(f"While {iterator} is less than {limit}...")
      print(f"\t{numbers} <== We push {iterator} into our array.\n")

      iterator = iterator + increment_Num
      print(f"\tThen increment iterator ({iterator - increment_Num}) by 'incrementNum' ({increment_Num}) to get {iterator}.\n")

  print(f"Our final array is: {numbers}.\n")

fill_array_with_numbers(1, 2, 12)
fill_array_with_numbers(0, 3, 80)
fill_array_with_numbers(80,3, 1)

def fill_array_using_range(increment_Num, limit):
  # numbers = []

  if increment_Num >= limit:
    print(f"Your iterator ({increment_Num}) can't exceed your limit ({limit}).")
    print("\tOtherwise the loop won't fail.")
    return
  elif increment_Num < 1:
    print("Your iterator must be greater than 0.\n")
    return

  numbers = list(range(0, limit, increment_Num))

  print(f"Our final array is: {numbers}.\n")

fill_array_using_range(12, 144)
# fill_array_using_range(33, 12)
# fill_array_using_range(0, 12)