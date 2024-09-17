# 图书还书系统
# 每次可以归还1本书：abc
# 默认归还之间是没有书的
# 控制台输出：现在有书: abc
# 再次归还图书：zxc
# 控制台会输出：现在有书: abc zxc

# 用户输入归还书名

total = "现在有书："


def calc_total():
    global total
    return_book = input("请输入归还的书名：")
    total = total + " " + return_book
    print(total)


calc_total()
calc_total()
