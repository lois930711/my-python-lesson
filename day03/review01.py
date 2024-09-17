# 小明有一辆车，油箱加满油是60L
# 车子的油耗是 14L/100KM
# 小明要开车去游玩，每次开车前都会根据自己的路途路线的距离，进行油量预估，防止油不够。

# 现在写一个函数，实现以下功能：
# 通过调用函数 plan_trip() 来进行一次完整旅途规划
# 每一次旅途规划的流程如下：
# 1. 询问提示“请问本次旅途的距离是多少？”，并要求输入路途的距离
# 2. 根据油耗计算本次旅途会消耗多少L油，以及还剩多少油。
# 3. 控制台提示：你本次旅途消耗了XL油，你的邮箱还有XL油。
# 4. 第2次旅途规划开始，重复步骤1。

OIL_box = 60
fuel_consumption = 14


def plan_trip():
    global OIL_box
    distance = float(input("请问本次旅途的距离是多少？"))
    oli_use = distance / 100 * fuel_consumption
    OIL_box = OIL_box - oli_use
    print("你本次旅途消耗了"+str(oli_use)+"L油, 你的邮箱还有"+str(OIL_box)+"L油")


plan_trip()
plan_trip()
