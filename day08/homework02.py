from typing import List, Tuple
from mock_data import user_list
# 题目2
# 队列规划问题
# 某办事大厅有5个办事窗口
# 该办事大厅可以处理的事务和所需时间如下：
# 1. 办理出生证（30分钟）
# 2. 办理房产证（80分钟）
# 3. 办理护照（25分钟）
# 4. 办理无犯罪记录证明（10分钟）
# 5. 办理结婚证（60分钟）
# 先有一个办事人员 list，里面的 tuple 表示姓名和办理的事务，例如：
# user_list = [
#     ("宋慧乔", '办理房产证'),
#     ("周杰伦", '办理护照'),
#     ...
# ]
# 请提前给按照 list 顺序给他们安排好去哪个窗口，以保证5个窗口每个窗口工作的时间都差不多。
# 例如：
# 窗口1：宋慧乔（办理房产证，80分钟）
# 窗口2：周杰伦（办理护照， 25分钟）
# 窗口3：杨超越（办理房产证， 80分钟）
# 窗口4：刘亦菲（办理结婚证, 60分钟）
# 窗口5：吴亦凡（办理无犯罪记录证明， 10分钟）
# 此时，后面还有2个人  ("郭敬明", '办理护照')  ("沈腾", '办理出生证')
# 按照描述的逻辑，郭敬明应该去窗口5，此时窗口5的工作总时间变为了35分钟，
# 沈腾去窗口2，窗口2的工作总时间变成了55分钟...以此类推
# 此函数期望输出结果举例如下：
# queues = [
#     # list 中包含 tuple，
#     # 每个 tuple 表示一个窗口
#     # tuple 第1个值是1个 list，里面是排队的人员的 tuple
#     # 第2个参数是 int，表示这个窗口工作的总时间
#     ([("宋慧乔", '办理房产证'), ("周杰伦", '办理护照'), ...], 500),
#     ([("杨超越", '办理结婚证'), ("刘亦菲", '办理出生证'), ...], 490),
#     ([("吴亦凡", '办理护照'), ("郭敬明", '办理无犯罪记录证明'), ...], 680),
#     ...
# ]


# def queue_up(list: List[Tuple[str, str]]) -> List[Tuple[List[Tuple[str, str]], int]]:
#     pass


# ! IMPORTANT 值类型和引用类型的区别：
# user_name = "Jack"  # 值类型, str, int, float, bool， tuple
# 引用类型， list dict set function，存的都是这个变量指向内存的地址 < 0xfjadjfi23dd>
# user_list = ["Jack", "Bob"]
# user_list2 = user_list
# user_list2.append("wallace")
# print(user_list, user_list2)


def get_time(affair):
    if affair == '办理出生证':
        return 30
    if affair == '办理房产证':
        return 80
    if affair == '办理护照':
        return 25
    if affair == '办理无犯罪记录证明':
        return 10
    if affair == '办理结婚证':
        return 60


def queue_up(user_list):
    window_user_list = [[], [], [], [], []]
    window_cumulative_time = [0, 0, 0, 0, 0]

    for user_list_item in user_list:

        the_least_queue_index = 0
        the_least_queue_value = window_cumulative_time[the_least_queue_index]
        for window_cumulative_time_item_index, window_cumulative_time_item in list(enumerate(window_cumulative_time)):
            if window_cumulative_time_item < the_least_queue_value:
                the_least_queue_index = window_cumulative_time_item_index
                the_least_queue_value = window_cumulative_time_item

        window_user_list[the_least_queue_index].append(user_list_item)

        window_cumulative_time[the_least_queue_index] += get_time(
            user_list_item[1])

    return list(zip(window_user_list, window_cumulative_time))


print(queue_up(user_list))
print('----- end -----')


def queue_up2(user_list):
    window_user_list = [[], [], [], [], []]
    window_cumulative_time = [0, 0, 0, 0, 0]

    for user_list_item in user_list:
        the_least_index = window_cumulative_time.index(
            min(window_cumulative_time))
        window_user_list[the_least_index].append(user_list_item)
        window_cumulative_time[the_least_index] += get_time(user_list_item[1])

    return list(zip(window_user_list, window_cumulative_time))


print(queue_up2(user_list))
