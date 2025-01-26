class BaseClass:
    def method_base(self):
        print("Method from BaseClass")

class IntermediateClass(BaseClass):
    def method_intermediate(self):
        print("Method from IntermediateClass")

class DerivedClass(IntermediateClass):
    def method_derived(self):
        print("Method from DerivedClass")

obj = DerivedClass()
obj.method_base()  # Output: Method from BaseClass
obj.method_intermediate()  # Output: Method from IntermediateClass
obj.method_derived()  