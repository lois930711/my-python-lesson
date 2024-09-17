from mock_data import student_list
# 题目1
# 兴趣社团分组问题
# 给定一个学生 list，里面是包含学生姓名，性别，兴趣社团的 tuple，
# 例如：
# student_list = [
#     ("李白", "男", "文学社"),
#     ("易建联", "男", "篮球社"),
#     ...
# ]
# 期望得到一个统计 list，包含了兴趣班和对应人数的 tuple，
# 例如：
# club_statistics = [
#     ("文学社", 2),
#     ("篮球社", 1),
#     ("烹饪班", 4)
#     ...
#
# def group_club(list: List[Tuple[str, str, str]]) -> List[Tuple[str, int]]:
#     pass


# 解题思路，先将数组拆解，用三个变量去一一接收数组中的元组，再统计数组中的第三位数量，在返回

def group_club(student_list):
    start_index = 0
    stop_index = len(student_list)
    社团 = []  # [文学社，文学社]
    社团集合 = []  # 【（文学社，1）（文学社，】
    club_statistics = []

    while True:
        _, _, club = student_list[start_index]  # 用club提取列表中的社团字段，“文学社”
        社团.append(club)  # 将club字段统一放进社团数组，[文学社]
        # num2 = len(list(filter(lambda item: item[2] == club, student_list)))
        num = 社团.count(club)  # 1，2
        # print(num)
        元组 = (club, num)  # （文学社，1）（文学社，2）
        print(元组)
        # if len(list(filter(lambda shetuan: shetuan[0] == 元组[0], 社团集合))) == 0:
        #     社团集合.append(元组)
        #     # club_statistics.append(元组)
        找到的社团_index = None
        for 社团集合_item_index, 社团集合_item in list(enumerate(社团集合)):
            if 社团集合_item[0] == 元组[0]:
                找到的社团_index = 社团集合_item_index

        if 找到的社团_index == None:
            社团集合.append(元组)
        else:
            社团集合[找到的社团_index] = 元组

        start_index = start_index + 1
        if start_index == stop_index:
            break

    return 社团集合

    # def group_club(student_list):
    #     student_list = []
    #     for student in student_list:
    #         shetuan = student[2]
    #     club_statistics_num = student_list.count(shetuan)
    #     return [(shetuan, club_statistics_num)]
club_statistics = group_club(student_list)
print(club_statistics)
