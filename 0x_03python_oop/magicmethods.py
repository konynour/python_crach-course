 # Magic metthods = Dunder methods (double underscore methods) __init__, __str__, __add__, __sub__, __mul__, __truediv__, 
 # __floordiv__, __mod__, __pow__, __and__, __or__, __xor__, __lt__, __le__, __eq__,
 #  __ne__, __gt__, __ge__, __len__, __getitem__, __setitem__, __delitem__, __iter__,
 #  __next__, __contains__, __call__, __enter__, __exit__, __new__, __del__, __repr__, 
 # __hash__, __bool__, __format__, __dir__, __sizeof__, __class__, __instancecheck__,
 #  __subclasscheck__, __prepare__, __init_subclass__, __get__,
 #  __set__, __delete__, __getattribute__, __setattr__, __delattr__, __getattr__,
 # they allow developers to define custom behavior for objects.

class Person :
    def __init__(self, name , age ):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Person name is {self.name}, age is {self.age}"
    def __eq__(self, other):
        return self.age == other.age
    def __lt__(self, other):
        return self.age < other.age
    


# creating instances and printing the results
person_1=Person("nour",22)
person_2=Person("mohamed",22)
print(person_1)
print(person_1==person_2)
print(person_1<person_2)
print("-----------------------------------------------------------------------------------------------------")