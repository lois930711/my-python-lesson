# set 集合
# 类似 list，但是和 list 区别是，set 里面的元素不可以重复，
# 并且顺序不保证 fruit[0] ？ ⬅️ 不可以通过这种方式获取，无法直接获取，
# 但是可以通过 for in 来拿要的元素
fruit_set = {'apple', 'banana', 'peach', 'apple'}
# print(fruit_set)
fruit_set.add('melon')
# print(fruit_set)
fruit_set.add('melon')
# print(fruit_set)

empty_set = set()
empty_set.add('apple')

user_list = ['jack', 'bob', 'lois', 'jack', 'bob']
new_user_list = list(set(user_list))
# print(new_user_list)

# dict 字典
# 以前，我要表示一个学生信息，是不是元组？
# ('Lois', 18, 1, 1) <- 姓名，年龄，性别，学号

lois = ('Lois', 18, 1, 1)
lois[0]  # 获取到了名字

lois2 = {
    # key: value
    "name": "lois",
    "age": 18,
    "gender": 1,
    "no": 1
}
lois2["name"]


# def get_time(affair):
#     if affair == '办理出生证':
#         return 30
#     if affair == '办理房产证':
#         return 80
#     if affair == '办理护照':
#         return 25
#     if affair == '办理无犯罪记录证明':
#         return 10
#     if affair == '办理结婚证':
#         return 60
#
# time = get_time("办理出生证")

affair_time_dict = {
    "办理出生证": 30,
    "办理房产证": 80,
    # ...
}

affair_time_dict['办理出生证']

empty_dict = {}
# print(empty_dict)
empty_dict["name"] = "Jack"
# print(empty_dict)
# print(empty_dict['name'])
# print(empty_dict.get("name"))
