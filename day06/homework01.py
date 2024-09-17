# 题目1：
# 函数功能：
# 第一个参数是一个数组，第二个参数是指定的姓
# 删除数组中，名字包含姓的名字
# def delete_user_include_last_name():
#     # 请完成此函数
#     pass

# 调用结果参考：
# filtered_user_list = delete_user_include_last_name(['王晓栋', '王由之', '唐振炀', '路思佳', '余娇娇', '朱琳云'], '王')
# 最后输出 filtered_user_list 的值期望为：['唐振炀', '路思佳', '余娇娇', '朱琳云']

# def delete_user_include_last_name(name_list, last_name):
#     def filter_helper(item):
#         # [start_index : stop_index(不包含) : step(步长，不写默认是1)]
#         return not item[0: len(last_name)] == last_name
#     # ⬇️ 简写成 lambada 表达式
#     # lambada item : not item[position:position+len(last_name)] == last_name

#     filterd_name = list(filter(filter_helper, name_list))
#     return filterd_name


# filtered_user_list = delete_user_include_last_name(
#     ['王晓栋', '王由之', '唐振炀', '路思佳', '余娇娇', '朱琳云'], '王')
# print(filtered_user_list)

# filtered_user_list1 = delete_user_include_last_name(
#     ['王由之', '路思佳', '罗小王'], '王')
# print(filtered_user_list1)


def xx(user_name_list, last_name):
    current_index = 0
    stop_index = len(user_name_list)

    filtered_user_name_list = []

    while True:
        current_user_name = user_name_list[current_index]
        if current_user_name[0:len(last_name)] != last_name:
            filtered_user_name_list.append(current_user_name)

        current_index = current_index + 1

        if current_index == stop_index:
            break

    return filtered_user_name_list


print(xx(['王由之', '路思佳', '罗小王'], '王'))
