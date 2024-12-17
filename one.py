import sys

# Set default encoding to UTF-8 for standard output
sys.stdout.reconfigure(encoding='utf-8')

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand
    
    def move(self):
        print(f"{self.name} is driving 🚗")

class Plane(Vehicle):
    def __init__(self, name, airline):
        super().__init__(name)
        self.airline = airline
    
    def move(self):
        print(f"{self.name} is flying ✈️")

class Boat(Vehicle):
    def __init__(self, name, type_of_boat):
        super().__init__(name)
        self.type_of_boat = type_of_boat
    
    def move(self):
        print(f"{self.name} is sailing 🚤")

class Bicycle(Vehicle):
    def __init__(self, name, type_of_bicycle):
        super().__init__(name)
        self.type_of_bicycle = type_of_bicycle
    
    def move(self):
        print(f"{self.name} is pedaling 🚲")

# Instantiate objects
car = Car("Sedan", "Toyota")
plane = Plane("Boeing 747", "Airways")
boat = Boat("Yacht", "Luxury")
bicycle = Bicycle("Mountain Bike", "Off-road")

# Call move() on each object
vehicles = [car, plane, boat, bicycle]
for vehicle in vehicles:
    vehicle.move()
