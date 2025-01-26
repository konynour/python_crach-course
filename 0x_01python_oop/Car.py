#inheritance example in python 
#class Car is the parent class
#class main is the child class
#main class inherits the Car class
#main class has the same methods as the Car class
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"You drive the {self.color} {self.model}.")

    def stop(self):
        print(f"You stop the {self.color} {self.model}.")

    def describe(self):
        print(f"{self.model}, {self.color}, {self.year}")
