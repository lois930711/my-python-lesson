def chinese_names_plus(chinese_names):
    name = 0
    chinese_names_len = len(chinese_names)

    if chinese_names_len == 0:
        return

    while True:
        print(chinese_names[name]+"酱")
        name = name + 1

        if name == chinese_names_len:
            break


chinese_names = ["李伟", "王芳", "张伟", "刘洋", "陈杰", "杨静", "赵强", "黄敏", "周磊",
                 "吴霞", "徐磊", "孙娜", "马丽", "朱涛", "胡婷", "郭勇", "何峰", "高燕", "林琳", "罗强"]
chinese_names_plus(chinese_names)
