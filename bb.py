# 第一个函数：计算圆的面积
# 第二个函数：计算这个圆对应的球体的体积
# PI 为常量，全局定义为 3.14

PI = 3.14


def calc_圆的面积(r):
    return PI * r ** 2


def calc_V(r):
    return 4/3 * PI * r ** 3

# 今日菜价五花肉n元，需要买x斤


def calc_foods(meat_unit_price, weight):
    return meat_unit_price*weight

# 计算每天家里的恩格尔系数


def Engel_coefficient(foods_daliy, income_daliy):
    return foods_daliy/income_daliy
