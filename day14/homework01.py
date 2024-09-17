# 抽象类定义
# Animal
# 属性有 name, gender, age

# 基本类定义
# Dog
# 继承 Animal
# 属性有 name, gender, age
# 方法有 bark（调用打印汪汪汪+名字）

# 基本类定义
# Cat
# 继承 Animal
# 属性有 name, gender, age
# 私有属性有 sterilization_status（绝育状态），默认为 False
# 方法1 meow（调用打印喵喵喵+名字）
# 方法2 sterilize（调用打印绝育成功，并且将私有 sterilization_status 设为 True）
# 方法3 mate（如果 sterilization_status 为 True，调用打印不能交配，否则调用打印交配成功）
# 方法4 get_sterilization_status（根据私有属性 sterilization_status（绝育状态），打印“喵喵已绝育”或者“喵喵未绝育”）

class Animal:
    def __init__(self, name: str, gender: str, age: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age


class Dog(Animal):
    def __init__(self, name, gender, age) -> None:
        super().__init__(name, gender, age)

    def bark(self):
        print("汪汪汪", self.name)


class Cat(Animal):
    def __init__(self, name, gender, age) -> None:
        super().__init__(name, gender, age)

    __sterilization_status = False

    def meow(self):
        print("喵喵喵", self.name)

    def sterilize(self):
        print("绝育成功")
        self.__sterilization_status = True

    def mate(self):
        if self.__sterilization_status == True:
            print("不能交配")
        else:
            print("交配成功")

    def get_sterilization_status(self):
        if self.__sterilization_status == True:
            print("喵喵已绝育")
        else:
            print("喵喵未绝育")


lachang = Dog("吴彦祖", "母", 12)
lachang.bark()


bigg = Cat("胖虎", "母", 7)
bigg.meow()
bigg.get_sterilization_status()
bigg.sterilize()
bigg.get_sterilization_status()
bigg.mate()
