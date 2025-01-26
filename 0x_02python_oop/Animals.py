class Animals:  # Superclass
    def __init__(self, name):  # Constructor
        self.name = name  # Instance variable

    def eat(self):  # Instance method
        print(f"{self.name} is eating")  # Accessing instance variable

    def sleep(self):  # Instance method
        print(f"{self.name} is sleeping")  # Accessing instance variable


class Prey(Animals):  # Subclass of Animals
    def flee(self):  # Instance metho
        print(f"{self.name} is fleeing")  

class Predator(Animals):  # Subclass of Animals
    def hunt(self):  # Instance method
        print(f"{self.name} is hunting") 


class Rabbit(Prey):  # Subclass of Prey
    pass  # Null statement


class Hawk(Predator):  # Subclass of Predator
    pass 


class Fish(Prey, Predator):  # Subclass of both Prey and Predator
    pass  


# Creating objects of the subclasses
rabbit = Rabbit("Rabbit")  # Object of Rabbit class
hawk = Hawk("Hawk")  
fish = Fish("Fish")  

# Using methods from the objects
rabbit.eat()  
rabbit.flee()

hawk.eat()  
hawk.hunt()

fish.eat()  
fish.hunt()  
fish.flee()  
