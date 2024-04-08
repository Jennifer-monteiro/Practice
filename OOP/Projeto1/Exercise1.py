""" 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
 """
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        dob_date = datetime.strptime(self.dob, '%Y-%m-%d')
        current_date = datetime.now()
        age = current_date.year - dob_date.year

        return age
    
person1 = Person('Jen', "usa", "1993-01-25")
person2 = Person('aa', "BR", "1997-01-25")
person3 = Person('bb', "CD", "1983-01-25")

print("Age of", person1.name,':', person1.calculate_age())
print("Age of", person2.name,':', person2.calculate_age())
print("Age of", person3.name,':', person3.calculate_age())