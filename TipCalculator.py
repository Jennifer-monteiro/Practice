print("Welcome to the tip Calculator/n")
price = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip = tip/100


tip_total =  (price * tip) 
total = (price + tip_total) / people

print(f" Each person should pay {total}")