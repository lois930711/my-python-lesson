# 通过 input() 方法和 while 循环
# 让用户每一轮循环输入1个数字，
# 将用户的输入的所有的数字保存到数组，并且将整个数组反转
# 如果某一轮用户输入的是 “end” 字符串，就跳出循环，打印上面反转后的结果
# 您输入的正向顺序是：[1, 2, 3]
# 您输入的反向顺序是：[3, 2, 1]

# def num_game():
#     user_nubjihefan = []
#     user_nubjihezheng = []
#     while True:
#         user_nub = int(input("请输入一个数字:"))
#         user_nubjihezheng.append(user_nub)
#         print(user_nubjihezheng)
#         if user_nub == "end":
#             print(user_nubjihefan)
#             break
#         user_nubjihefan.insert(0, user_nub)


# num_game()


def num_game():
    user_nubjihe = []
    while True:
        user_nub = input("请输入一个数字:")
        if user_nub == "end":
            reversed_user_nubjihe = user_nubjihe[::-1]
            print("您输入的正向顺序是：", user_nubjihe)
            print("您输入的反向顺序是：", reversed_user_nubjihe)
            break
        user_nubjihe.append(int(user_nub))


num_game()
