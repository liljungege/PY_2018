class Student():
    name = '张安'
    age = 0

    def __init__(self, name, age):
        # 构造函数
        # 初始化对象属性
        self.name = name
        self.age = age
        # print("student")
    # def print_file(self):
    #     print("name: " + self.name)
    #     print("age: " + str(self.age))
    def do_homework(self):
        print("homework")
# student = Student()
# student.print_file()