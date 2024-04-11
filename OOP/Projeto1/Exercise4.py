""" OOP Exercise 5: Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise. """

class vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vehicle):
    pass

class Car(vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
audi = Car("Audi Q5", 240, 18)

print("Color: ",school_bus.color, ",", "Vehicle name: ", school_bus.name)