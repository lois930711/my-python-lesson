from mock_data import student_list
# [("李白", "男", "文学社"), ...]
# [("文学社", 2), ...]


# def calc_club_num(student_list):
#     start_index = 0
#     stop_index = len(student_list)
#     club_list = []
#     result = []
#     while True:
#         _, _, club = student_list[start_index]
#         club_list.append(club)
#         num = len(list(filter(lambda item: item[2] == club, student_list)))
#         tuple_club = (club, num)

#         if len(list(filter(lambda item: item[0] == club, result))) == 0:
#             result.append(tuple_club)

#         start_index += 1
#         if start_index == stop_index:
#             break
#     print(result)


def calc_club_num(student_list):
    result = []

    for student_list_item in student_list:
        _, _, club = student_list_item
        num = len(list(filter(lambda item: item[2] == club, student_list)))
        tuple_club = (club, num)

        if len(list(filter(lambda item: item[0] == club, result))) == 0:
            result.append(tuple_club)
    print(result)


calc_club_num(student_list)
