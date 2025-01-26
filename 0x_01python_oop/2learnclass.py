class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

# Creating an instance of the Person class
person1 = Person("Ali", 25)  # Added a comma between "Ali" and 25
person2 = Person("Sarah", 30)

# Printing the attributes of person1
print(person1.name,person1.age)
print(person2.name,person2.age)
