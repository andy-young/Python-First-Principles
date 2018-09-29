# Comment above each line, explaining what is happening to the line below
# The integer 100 is assigned to the variable 'car'
cars = 100
# The space available for a passenger in each car
space_in_car = 4.0
# The number of people available to drive a car
drivers = 30
# The number of non-drivers who need available space in a car
passengers = 90
# The number of cars not driven is equal to the number of cars in the fleet
# minus the number of available drivers
cars_not_driven = cars - drivers
# A car is 'driven' when a 'driver' operates it
cars_driven = drivers
# The total amount of available space in the entire fleet of cars
carpool_capactiy = cars_driven * space_in_car
# Because each car needs a driver, dividing that into the number of passengers
# gives us the average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capactiy, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# What you should see when the code is ran:
# There are 100 cars available.
# There are only 30 drivers available.
# There will be 70 empty cars today.
# We can transport 120.0 people today.
# We have 90 to carpool today.
# We need to put about 3.0 in each car.

# Study Drills
# 1. Try running python3 from the Terminal as a calculator
# .. and use variable names to do your calculations.
