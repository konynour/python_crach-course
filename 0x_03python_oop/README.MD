 Python does not support method overloading in the traditional sense like some other programming languages like Java or C++.
 polymorphism =Greek word that meeans to have many forms of faces
 poly=many
 morphism =form
 -------------------------------------------------------------------------------------

ex for overloading

class Example:
     def method(self, a):
         print(f"Method with one argument: {a}")

     def method(self, a, b):
         print(f"Method with two arguments: {a}, {b}")

 obj = Example()
 obj.method(10)  # TypeError: method() missing 1 required positional argument
 obj.method(10, 20)  # Only the second definition work
 ------------------------------------------------------------------------------------

 static methods =  A static method is a method that belongs to a class rather than an instance. It does not require self or cls as a parameter because it does not operate on a specific instance or the class itself.
 instance methods = An instance method is a method that operates on an instance of the class. It requires an instance of the class to be called and can access and modify the instance's attributes.
 First Parameter: The first parameter of an instance method is always self, which refers to the instance that is calling the method.
magic methods = Dunder methods (double underscore)__init__,__str__,__eq__
                they are automatically called by many of python`s built-in operations.
                they allow developers to define or customiza the behavior of objects
