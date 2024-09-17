import random
print(range(0, 10))


def random_line(length):
    magic_line = "".join(random.choice("01")for _ in range(length))
    return magic_line


def random_hight(hight, length):

    for _ in range(hight):
        print(random_line(length))


random_hight(4, 130)


fruit_list = ["apple", "peach"]


class Fruit(可迭代协议):
    def __init__(self) -> None:
        super().__init__()
        pass

    __fruit1 = "apple"
    __fruit2 = "peach"

    __iter__()

    __next__()


my_fruit = Fruit()
my_fruit[0]
