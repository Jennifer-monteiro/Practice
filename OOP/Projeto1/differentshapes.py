""" Design classes for different shapes like Circle,  and Triangle. 
Implement methods to calculate the area and perimeter of each shape. """
import math
class Circle:

    def __init__(self,radius):
        self.radius = radius

    def circunference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return (f"A area do circulo é: {round(self.area(),2)}, "
                f" A circunferencia é: {round(self.circunference(),2)}")
                

class Triangle:
    def __init__(self, side1, side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        return f"O perimeter of a Triangule is {self.perimeter()}"

triangle = Triangle(3,4,5)
print("O perimetro do triangule é:", triangle.perimeter())
print(triangle)
circle = Circle(10)
print(f"A area do circulo é: {circle.area()}, "
    f" A circunferencia é: {circle.circunference()}")
print(circle)