# 条件判断
# 偏低 小于等于18.5
# 正常 在18.5-24之间
# 超重 24-28之间
# 肥胖 大于 28

def get_bmi_text(bmi):
    if bmi <= 18.5:
        print('偏低')
    elif bmi > 18.5 and bmi <= 24:
        print('正常')
    elif bmi > 24 and bmi <= 28:
        print('超重')
    else:
        print('肥胖')


get_bmi_text(18)


# 以 if 开始第一个判断
# 以 else 结束

# 患者
patient_age = 60
patient_bmi = 29

# 如果患者的年龄 > 55 或者患者的 bmi > 28
# 就调用 push_to_doctor()


def check_body_status(age, bmi):
    if age > 55 or bmi > 28:
        print('调用了 push_to_doctor()')


check_body_status(patient_age, patient_bmi)


def check_body_status2(age, bmi):
    if age > 55:
        print('调用了 push_to_老年科医生()')
    if bmi > 28:
        print('调用了 push_to_肥胖科医生()')


check_body_status2(patient_age, patient_bmi)
