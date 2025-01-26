class student:
    school_name="global high school"  # Class variable
    def __init__(self,name,age):
        self.name=name # Instance variable
        self.age=age # Instance variable

student1= student("Ali",22)
student2= student("Sara",23)

print(student1.school_name)
print(student2.school_name)

student.school_name="national high school"
print(student1.school_name) # Output: national high school
print(student2.school_name) # Output: national high school
