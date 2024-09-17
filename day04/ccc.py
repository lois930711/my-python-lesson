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

# 新增内容
# 汽车油箱的练习
# 当油量小于 30 的时候，print 提示：油不多啦
# 当某次 plan_trip() 计算油量小于0，提示：你的油不够本次旅行。

def plan_trip():
    oil_box = 60
    youhao = 14

    while True:
        distance = float(input("请问本次旅途的距离是多少？"))
        xiaohao = distance / 100 * youhao
        oil_box = oil_box - xiaohao
        if oil_box >= 30:
            print("根据油耗计算本次旅途会消耗", xiaohao, "L油,以及还剩", oil_box, "油")
        elif oil_box < 30 and oil_box > 0:
            print("油不多啦，还剩下", oil_box)
        else:
            print("你的油不够本次旅行。")
            break


plan_trip()
