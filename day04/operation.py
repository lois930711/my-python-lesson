#


def doctor_operation():
    pt_name = input('ptname: ')
    print('手术单已经创建')

    def start():
        print(pt_name + "的手术开始了")

    return start()  # = None


start = doctor_operation()  # None

# 假设过了10分钟
print("假设过了10分钟")
start()
