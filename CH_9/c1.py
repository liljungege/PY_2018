class Student():
    # name = '张安'
    # age = 0
    sum = 0

    def __init__(self, name, age):
        # 构造函数
        # 初始化对象属性
        self.name = name
        self.age = age
        self.score = 0
        Student.sum += 1
        print(Student.sum)
        # print("student")
    # def print_file(self):
    #     print("name: " + self.name)
    #     print("age: " + str(self.age))
    def do_homework(self):
        self.do_english()
        print("homework")

    def do_english(self):
        print("da")
    
    def marking(self, score):
        if score <0:
            score = 0
        self.score = score
        print(self.score)

    @classmethod # 装饰器
    def plus_sum(cls): # cls代表类本身
        cls.sum += 1
        print(cls.sum)
    
    @staticmethod
    def add(x, y):
        pass
        

