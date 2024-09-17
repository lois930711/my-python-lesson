# # 用户信息 tuple:
# # (姓名, 年龄, 邮箱)
# user_info = ("John", 25, "john@example.com")


# # 练习
# # 将用户信息转为字典
# def convert_tuple_to_dict(user_info):
#     pass


# # 测试
# user_info_dict = convert_tuple_to_dict(user_info)
# print("user_info_dict: ")
# print(user_info_dict)
# print("----- divider -----")


def convert_tuple_to_dict(user_info):
    user_info_dict = {
        "姓名": user_info[0],
        "年龄": user_info[1],
        "邮箱": user_info[2]
    }
    return user_info_dict


user_info = ("John", 25, "john@example.com")
user_info_dict = convert_tuple_to_dict(user_info)
print("user_info_dict: ")
print(user_info_dict)
print("----- divider -----")
