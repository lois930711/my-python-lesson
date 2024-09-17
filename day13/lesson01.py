

# 今日课程内容：
# 面向对象

# student_dict = {
#     "name": "Jack",
#     "age": 18,
#     "gender": 1,
#     "hobbies": ["Swimming", "Football"]
# }


# def introduce_myself(student_dict):
#     print("我的名字叫", student_dict["name"], "，我今年",
#           str(student_dict["age"]), "岁啦")


# introduce_myself(student_dict)

# 类 class

# 创建一个类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("我的名字叫：", self.name)


jack = Student("Jack", 18)
bob = Student("Bob", 15)

jack.introduce()
bob.introduce()
