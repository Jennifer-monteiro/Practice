class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'


    def speak(self,sound):
        return f"{self.name} says {sound}"

    
dog1 = Dog("Philo", 12)
dog2 = Dog("AAH", 13)
dog3 = Dog("bbb", 5)

print(dog1)
print(dog2)
print(dog3)

print(dog1.speak("auau"))
print(dog2.speak("bbb"))
print(dog3.speak("ccc"))