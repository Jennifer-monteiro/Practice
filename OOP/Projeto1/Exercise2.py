class Calculator:
    def add(self,x,y):
        return x + y
    
    def subtract(self,x,y):
        return x- y
    
    def multiply(self,x,y):
        return x*y
    
    def division(self,x,y):
        return x/y
    
calculator = Calculator()

print("add", calculator.add(10,5))
print("Minus", calculator.subtract(20,2))
print("Multiplication", calculator.multiply(2,5))