
from mock_data import student_list


def calc_count(student_list):

    current_index = 0
    stop_index = len(student_list)
    woman_count = 0
    man_count = 1

    while True:
        current_student = student_list[current_index]
        _, gender, _ = current_student

        if gender == 0:
            woman_count += 1
        else:
            man_count += 1  # 写法等于 man_count = man_count + 1

        if current_index == stop_index:
            break

    return [('男', man_count), ('女', woman_count)]
