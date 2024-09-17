# 从 mock_data 中导入 student_list
# student_list 内，每个 tuple 结构表示（姓名，性别0女1男，兴趣班）
# 分别写函数，完成以下功能：
# 1. 函数1
# 统计男女分别多少，例如输出：[("男", 20), ("女", 80)]
# 2. 函数2
# 将 student_list 内部的 tuple 中的性别转换为中文
# 转换后，例如输出：[("张伟", "女", "美术社"), ("王洋", "男", "音乐社"), ...]
# 3. 函数3
# 按照性别分组学生，输出例如：
# [
#  [("张伟", 0, "美术社"), ...], # 女一组
#   [("王洋", 1, "音乐社"), ...]  # 男一组，把2个数组再放到一个大数组里返回
# ]
