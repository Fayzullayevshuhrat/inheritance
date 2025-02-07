class Person:
    def __init__(self, name,fam):
        self.name = name
        self.fam = fam
    def hi(self):
        print("hello")

class Pupil(Person):
    pass

class Student(Person):
    def study(self):
        print("studying")


class Teacher(Person):
    def teach(self):
        print("teaching")

p = Student("A", "B")
p.hi()