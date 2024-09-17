# 今日菜价五花肉n元，需要买x斤
# 计算每天家里的恩格尔系数

def calc_foods(meat_unit_price, weight):
    return meat_unit_price*weight


def Engel_coefficient(foods_daliy, income_daliy):
    return foods_daliy/income_daliy


today = calc_foods(25, 2)
today0829 = Engel_coefficient(today, 1000)

print(today)
print(today0829)
