""" Creating a Simple Class:
Define a class called Rectangle. It should have attributes width and height and methods to calculate its area and perimeter. """

class Rectangle:
    def __init__(self,name,width, height):
        self.width = width
        self.height = height
        self.name = name

    def result(self):
        return self.width * self.height
    
    def __str__(self):
        return f'The area of {self.name} is {self.result()}'

# Creating instances of Rectangle
rectangle1 = Rectangle("Rectangle 1", 5, 6)
rectangle2 = Rectangle("Rectangle 2", 10, 6)
rectangle3 = Rectangle("Rectangle 3", 11, 6)
rectangle4 = Rectangle("Rectangle 4", 12, 6)

print(rectangle1.result())

print(rectangle1)