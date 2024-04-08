""" Write a Python program to create a Vehicle class with max_speed 
and mileage instance attributes.
 """

class Car:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car1 = Car(20,5)
car2 = Car(100,63)
car3 = Car(250,51)
car4 = Car(200,4)

print("Your Max Speed is: ", car1.max_speed, "\nYour mileage is: ", car1.mileage)
print("Your Max Speed is: ", car2.max_speed, "\nYour mileage is: ", car2.mileage)
print("Your Max Speed is: ", car3.max_speed, "\nYour mileage is: ", car3.mileage)
print("Your Max Speed is: ", car4.max_speed, "\nYour mileage is: ", car4.mileage)
