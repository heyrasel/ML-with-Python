class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll


    def display(self):
        print(f"Name: {self.name}\nRoll No: {self.roll}")

student = Student("John",2)
student.display()