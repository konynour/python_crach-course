class ClassA:
    def method_a(self):
        print("Method from ClassA")

class ClassB:
    def method_b(self):
        print("Method from ClassB")

class DerivedClass(ClassA, ClassB):
    pass

obj = DerivedClass()
obj.method_a()  # Output: Method from ClassA
obj.method_b()  # Output: Method from ClassB