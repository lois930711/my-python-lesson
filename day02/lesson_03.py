from bmi import calc_bmi

# pre. 变量类型
# 整数类型 int：     2，3650，291
# 浮点数（小数）float ： 1.03, 7.0
# 字符串 str：       "abc", "2"
# 布尔类型 bool:  True, False

# 变量的类型是什么？
# 由赋值的时候决定
# gender = '男'

# 1. 交互式输入
# 请输入你的体重
# 请输入你的身高

# user_weight = input('请输入体重')
# 此时，user_weight 读取到的只是用户输入的 str
# 因为后面需要进行计算，所以期望将用户输入的值转为 float
# 用 float(需要转换的数字字符串)
# float(user_weight)
user_weight = float(input('请输入体重'))
user_height = float(input('请输入身高'))

# 现在已经获取到了用户输入的体重和身高，
# 期望接下来帮用户计算他的 bmi 值，把结果返回告诉用户

user_bmi = calc_bmi(user_weight, user_height)
print(user_bmi)
