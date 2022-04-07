
class Calculator:
    #constructor
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    #addition
    def adder(self):
        addition = self.x + self.y
        print("Addition of x and y is", addition)
        return addition

    #subtraction
    def subtractor(self):
        difference =  self.x - self.y
        print("Subtraction of x and y is", difference)
        return difference

    #multiplication
    def multiplier(self):
        multiplication = self.x * self.y
        print("Multiplication of x and y is", multiplication)
        return multiplication

    #division
    def divider(self):
        division = self.x / self.y
        print("Division of x and y is", division)
        return division

    #clear to 0
    def clear(self):
        self.x = 0.0
        self.y = 0.0

#main
if __name__ == "__main__":
    calc = Calculator()
    #user input
    calc.x = float(input("Enter x: "))
    calc.y = float(input("Enter y: "))

    calc.adder()
    calc.subtractor()
    calc.multiplier()
    calc.divider()
    calc.clear()
    print("Reset numbers")
    print("x = ", calc.x)
    print("y = ", calc.y)


