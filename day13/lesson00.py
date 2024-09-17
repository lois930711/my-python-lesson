# 范型
# 规范参数传递的类型

def calc_operation(n1: int, n2: int, operation: str) -> int:
    pass


def fn2(list: list[str]):
    pass


# tuple  => ("jack", 18)
def fn2(list: list[tuple[str, int]]):
    pass
