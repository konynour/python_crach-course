class Student :
    def __init__(self, name , age ,grade):
        self.__name=name
        self.__age=age
        self.__grade=grade
    def get_name(self):
        return self.__name
        
    def set_name(self,new_name):
        self.__name=new_name

    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age=new_age

    def get_grade(self):
        return self.__grade
    def set_grade(self,new_grade):
        self.__grade=new_grade
    def describe(self):
        return f"Student name is {self.__name}, age is {self.__age}, and grade is {self.__grade}"
# Creating an instance and printing the result

student_1=Student("nour",22,90)
print(student_1.get_name())
student_1.set_name("mohamed")
print(student_1.get_name())
print("-----------------------------------------------------------------------------------------------------")

          