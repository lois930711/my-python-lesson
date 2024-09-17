def gender_chinese():
    for student_list_item in student_list:
        if student_list_item[0] == "0":
            student_list_item[0] == "女"
        else:
            student_list_item[0] == "男"
            break


student_list = [(0, 48), (1, 30)]
gender_chinese(student_list)
print(student_list)
