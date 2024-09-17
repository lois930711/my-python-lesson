def input_what_number():
    res = int(input('请输入数字'))

    if res > 0:
        return '正数'
    elif res < 0:
        return '负数'
    else:
        return '0'
