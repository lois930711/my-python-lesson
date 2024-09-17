# 复习
# 1. 元组
# 顺序不可变，元素不可变，可以多种类型
user_info = ('Tom', 20, '男')
# 如何访问元组中的元素
name, age, gender = user_info
# 如果只想获取第2个元素
age2 = user_info[1]

# 新知识点
# 2. 列表（数组）
# 声明一个列表
# 列表的特性
# 1. 放的类型是一致的
# 2. 里面的内容可变（包括内部元素和长度都可变）
user_list = ['Tom', 'Jack', 'BOB', 'Jack', 'Rose']
book_list = ['book1', 'book2']

# print(user_list)
# # 1. 内部元素变化
# user_list[0] = 'Wallace'
# print(user_list)
# # 2. 长度变化
# user_list.append("Lois")
# print(user_list)
# user_list.insert(0, "Obama")
# print(user_list)
# user_list.clear()
# print(user_list)

# user_list 的第3个元素删掉，期望得到的是 ['Tom', 'Jack', 'BOB', 'Rose']
# user_list.remove('Jack')
# print(user_list)
# user_list.pop(2)
# print(user_list)


del user_list[2]
print(user_list)
