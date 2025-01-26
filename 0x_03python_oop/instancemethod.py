class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):  # Instance method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an instance
person = Person("nour", 22)
print(person.greet()) 
