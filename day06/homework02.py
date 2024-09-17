# 题目2：
# 函数功能：
# 第1个参数是人员名字数组，比如：['王晓栋', '王由之', '唐振炀', '路思佳', '余娇娇', '朱琳云']
# 第2个参数是人员性别数组，比如：['男', '男', '男', '女', '女', '女']
# 第3个参数是人员年龄数组，比如：[32, 32, 32, 31, 30, 29]
# 这3个数组的信息顺序是对应的，每个数组的相同下表，表示的都是同一个人的信息，期望返回一个 list，
# list 中的每一项，都是一个 Tunple，按照(姓名, 性别, 年龄)的结构顺序，将对应的信息组合起来
# def combine_user_info():
#     pass

# 调用结果参考：
# name_list = ['王晓栋', '王由之', '唐振炀', '路思佳', '余娇娇', '朱琳云']
# gender_list = ['男', '男', '男', '女', '女', '女']
# age_list = [32, 32, 32, 31, 30, 29]
# combined_list = combine_user_info(name_list, gender_list, age_list)
# 最后输出 combined_list 的值期望为：[('王晓栋', '男', 32), ('王由之', '男', 32), ...等等]


# def combine_user_info(name_list, gender_list, age_list):
#     combined_list = list(zip(name_list, gender_list, age_list))
#     return combined_list


name_list = ['王晓栋', '王由之', '唐振炀', '路思佳', '余娇娇', '朱琳云']
gender_list = ['男', '男', '男', '女', '女', '女']
age_list = [32, 32, 32, 31, 30, 29]
# combined_list = combine_user_info(name_list, gender_list, age_list)
# print(combined_list)


def combine(name_list, gender_list, age_list):
    current_index = 0
    stop_index = len(name_list)

    temp_list = []

    while True:
        current_name = name_list[current_index]
        current_gender = gender_list[current_index]
        current_age = age_list[current_index]
        current_user_tuple = (current_name, current_gender, current_age)
        temp_list.append(current_user_tuple)

        current_index = current_index + 1
        if current_index == stop_index:
            break

    return temp_list


print(combine(name_list, gender_list, age_list))
