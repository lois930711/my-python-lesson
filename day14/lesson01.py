# 课程内容
# 面向对象，私有属性，私有方法，静态方法
class Student:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 私有属性
    # 服装品牌，不希望被外部修改和访问
    __cloth_brand = "Nike"

    def print_brand(self):
        # 内部方法可以访问和修改私有属性
        # self.__cloth_brand = "Adidas"
        print("服装品牌是：", self.__cloth_brand)

    def set_brand(self, brand):
        # 外部方法可以访问私有属性
        self.__cloth_brand = brand


jack = Student("Jack", 18, 178)
jack.print_brand()
jack.set_brand("Lining")
jack.print_brand()


class Teacher:
    def __init__(self):
        pass

    def say():
        print("hello")
