# dd = xxx.read_file("学生信息.xls")
# 学号 | 姓名 | 性别 | 年龄 | 语文成绩 | 数学成绩 | 英语成绩 | 政治 | 历史 | 地理 | 物理 | 化学 | 生物
# 1   | 张三 | 男   | 18   | 90      | 85      | 95
# 2   | 李四 | 女   | 19   | 80      | 90      | 85
# 3   | 王五 | 男   | 20   | 95      | 95      | 90


class Student:
    def __init__(self, id, name, gender, age, chinese_score, math_score, english_score):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.chinese_score = chinese_score

    def calc_myselft_average_score(self):
        return (self.chinese_score + self.math_score + self.english_score, self.地理) / 3


# student_list = xxx.convert(dd, Student, xx)
student_list = [
    # Student(1, "张三", "男", 18, 90, 85, 95),
    # Student(2, "李四", "女", 19, 80, 90, 85),
    # Student(3, "王五", "男", 20, 95, 95, 90)
]
jack = Student(1, "张三", "男", 18, 90, 85, 95)
bob = Student(2, "李四", "女", 19, 80, 90, 85)

student_list[0].name = "张三"
score = 0
for student in student_list:
    myself_averate_score = student.calc_myselft_average_score()
    score = score + myself_averate_score


average_score = score / len(student_list)
