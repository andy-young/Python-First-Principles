# Make a class named Animal that is-a(n) object
class Animal(object):
  pass

# Make a class named Dog that is-a(n) Animal
class Dog(Animal):

    def __init__(self, name):
        # from self, get the name attribute and set it to name
        self.name = name

# Make a class named Cat that is-a(n) Animal
class Cat(Animal):

    def __init__(self, name):
        # from self, get the name attribute and set it to name
        self.name = name

# Make a class named Person that is-a(n) object
class Person(object):

    def __init__(self, name):
        # from self, get the name attribute and set it to name
        self.name = name

        ## from self, get the pet attribute and set it to none
        self.pet = None

# Make a class named Employee that is-a Person
class Employee(Person):

      def __init__(self, name, salary):
          # Have Employee get attributes from Person Object
          super(Employee, self).__init__(name)
          # from self, get the salary attribute and set it to salary
          self.salary = salary

# Make a class named Fish that is-an Object
class Fish(object):
    pass

# Make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

# Make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass


# Set rover to an instance of class Dog, rover is-a Dog
rover = Dog("Rover")

# Set satan to an instance of class Cat, satan is-a cat
satan = Cat("Satan")

# Set mary to an instance of class Person, mary is-a person
mary = Person("Mary")

# from mary, get the pet attribute and set it to satan
mary.pet = satan

# Set frank to an instance of Class Employee that takes params "Frank" and 120000
frank = Employee("Frank", 120000)

# from frank, get the pet attribute and set it to rover
frank.pet = rover

# Set flipper to an instance of class Fish, flipper is-a Fish
flipper = Fish()

# Set crouse to an instance of class Salmon, crouse is-a Salmon
crouse = Salmon()

# Set harry to an instance of class Halibut, harry is-a Halibut
harry = Halibut()
