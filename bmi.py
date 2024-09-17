
# 题目：编写一个简单的体重指数（BMI）计算程序。
# 定义一个函数 calculate_bmi，它接受两个参数：weight（体重，单位：千克）和 height（身高，单位：米）。
# 在函数内部，使用 BMI 公式计算 BMI 值并返回。
# 定义几个变量，分别表示你的体重和身高。
# 调用函数，计算并输出 BMI 值。
def calc_bmi(weight_kg, height_m):
    return weight_kg/(height_m**2)
