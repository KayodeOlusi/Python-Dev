class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    
    def passed_semester(self):
        if self.gpa > 2.5:
            return True
        else:
            return False

student1 = Student("John", 34, 2.6)

print(student1.age)
print(student1.passed_semester())