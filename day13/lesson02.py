from abc import ABC, abstractmethod


class SchoolPerson(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def introduce(self):
        pass


class Human(ABC):
    @abstractmethod
    def cry(self):
        pass

    # @abstractmethod
    # def run(self):
    #     pass


class Teacher(SchoolPerson, Human):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def introduce(self):
        print("我是", self.name, "薪水是", self.salary)

    def cry(self):
        print('55555')


class Student(SchoolPerson, Human):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print("我叫：", self.name, "我的成绩是", self.grade)

    def cry(self):
        print('嘤嘤嘤')


wallace = Teacher("Wallace", 32, "100")
wallace.introduce()
# wallace.cry()

jack = Student("Jack", 18, "60")
jack.introduce()
# jack.cry()


def call_cry(stu: Student):
    stu.cry()


call_cry()
