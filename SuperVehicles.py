class Vehicle:
    def __init__(self, name:str, mpg:int):
        self.name = name
        self.mpg = mpg

    def fuel_needed(self, distance):
        return distance / self.mpg
    
    def description(self):
        return f"{self.name} get {self.mpg} miles per gallon."
    
class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)
        # dot-operator to refer to the function __init__ from the superclass: Vehicle.

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", 50)

class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 