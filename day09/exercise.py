# 从 mock_data 中导入 student_list
# student_list 内，每个 tuple 结构表示（姓名，性别0女1男，兴趣班）
# 分别写函数，完成以下功能：
# 1. 函数1
# 统计男女分别多少，例如输出：[("男", 20), ("女", 80)]
# 2. 函数2
# 将 student_list 内部的 tuple 中的性别转换为中文
# 转换后，例如输出：[("张伟", "女", "美术社"), ("王洋", "男", "音乐社"), ...]
# 3. 函数3
# 按照性别分组学生，输出例如：
# [
# 	[("张伟", 0, "美术社"), ...], # 女一组
#   [("王洋", 1, "音乐社"), ...]  # 男一组，把2个数组再放到一个大数组里返回
# ]

from mock_data import student_list
# 函数一（方法一）


def 计数器(student_list):
    girl_count = 0
    boy_count = 0
    for student_list_item in student_list:
        if student_list_item[1] == 0:
            girl_count = girl_count + 1
        else:
            boy_count = boy_count + 1
    print([("男", boy_count), ("女", girl_count)])


# 函数一（方法二）
def calc_gender(student_list):
    gender_num = []
    # start_index = 0
    # stop_index = len(student_list)
    统计 = []

    for student_list_item in student_list:
        _, gender, _ = student_list_item
        num = len(list(filter(lambda item: item[1] == gender, student_list)))
        if gender == 0:
            gender = "女"
        else:
            gender = "男"
        result = (gender, num)
        # print(result)
        # print("----")
        if len(list(filter(lambda item: item[0] == gender, 统计))) == 0:
            统计.append(result)
            # print(统计)
            # print("----")
        # start_index = start_index + 1

        # if start_index == stop_index:
        #     break
    return 统计


# 函数一（方法三)
def while_calc_gender(student_list):
    start_index = 0
    stop_index = len(student_list)
    gender_index = []
    统计 = []

    while True:
        _, gender, _ = student_list[start_index]
        # print(gender_index)
        num = len(list(filter(lambda item: item[1] == gender, student_list)))
        # print(num)
        if gender == 0:
            gender = "女"
        else:
            gender = "男"
        result = (gender, num)

        # print(result)
        if len(list(filter(lambda item: item[0] == gender, 统计))) == 0:
            统计.append(result)
        start_index = start_index + 1

        if start_index == stop_index:
            break
    return 统计


# 函数二（方法一）
def gender_chinese(student_list):
    name_index = []
    gender_index = []
    interest_index = []
    for student_list_item in student_list:
        name, gender, interest = student_list_item
        name_index.append(name)
        if gender == 0:
            gender = "女"
        else:
            gender = "男"
        gender_index.append(gender)
        interest_index.append(interest)
        result = list(zip(name_index, gender_index, interest_index))
    return result


# 函数二（方法二）
def gender_chinese1(student_list):
    copy_student_list = []
    for student_list_item in student_list:
        name, gender, interst = student_list_item
        # 此时 gender 是 int 类型
        gender_text = None
        if gender == 0:
            gender_text = "女"
        else:
            gender_text = "男"
        copy_student = (name, gender_text, interst)
        copy_student_list.append(copy_student)
    return copy_student_list


# 函数二（方法三）
def gender_chinese2(student_list):
    start_index = 0
    stop_index = len(student_list)
    copy_student_list = []

    while True:
        name, gender, interst = student_list[start_index]
        gender_text = None
        if gender == 0:
            gender_text = "女"
        else:
            gender_text = "男"
        copy_student = (name, gender_text, interst)
        copy_student_list.append(copy_student)

        start_index = start_index + 1
        if start_index == stop_index:
            break

    return copy_student_list

# 调用函数3(方法一)


def group_gender(student_list):
    gilr_group = []
    boy_group = []
    for student_list_item in student_list:
        if student_list_item[1] == 0:
            gilr_group.append(student_list_item)
        else:
            boy_group.append(student_list_item)
    print([gilr_group, boy_group])


# 调用函数3(方法二)
def group_gender1(student_list):
    start_index = 0
    stop_index = len(student_list)
    gilr_group = []
    boy_group = []

    while True:
        if student_list[start_index][1] == 0:
            gilr_group.append(student_list[start_index])
        else:
            boy_group.append(student_list[start_index])

        start_index += 1
        if start_index == stop_index:
            break

    print([gilr_group, boy_group])


# # 调用函数1(方法一)
# 计数器(student_list)
# print("------")

# # 调用函数1(方法二)
# 结果二 = calc_gender(student_list)
# print(结果二)
# print("------")

# # 调用函数1（方法三）
# 结果三 = while_calc_gender(student_list)
# print(结果三)
# print("------")

# # 调用函数2(方法一)
# result_list = gender_chinese(student_list)
# print(result_list)
# print("------")

# # 调用函数2(方法二)
# result_list1 = gender_chinese1(student_list)
# print(result_list1)
# print("------")

# # 调用函数2(方法三)
# result_list2 = gender_chinese2(student_list)
# print(result_list2)
# print("------")

# # 调用函数3(方法一)
# group_gender(student_list)

# 调用函数3(方法二)
group_gender1(student_list)
