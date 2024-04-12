""" Animal Kingdom:
Create a class called Animal. Each animal should have attributes like name,
 age, and sound. Implement methods to make the animal speak and
 to display its information. """

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        return f'{self.name} says: "{sound}"'
    
    def __str__(self):
        return f"{self.name}, is {self.age}"

animal1 = Animal("Karl", 20)
animal2 = Animal("Bianca", 30)
print(animal1)
print(animal2)

print(animal1.speak("woof"))
