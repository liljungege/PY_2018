from c4 import Human

class Student(Human):
    # sum = 0
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)
    #     self.name = name
    #     self.age = age
    #     self.score = 0
    #     Student.sum += 1
    
    def do_homework(self):
        super(Student, self).do_homework()
        print("English Homework")
    
student1 = Student("人民小学", "喜小乐", 18)
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
student1.do_homework()


