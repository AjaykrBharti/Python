"""Create Student class and create an object to it. and display student detials"""


class Student:
    def __init__(self):
        self.name="Ajay Kumar"
        self.age = 23

    def display(self):
        print("Student Details : ")
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)

one = Student()
one.display()
two = Student()
two.display()
