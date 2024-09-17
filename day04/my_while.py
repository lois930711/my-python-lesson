#

def run_geuss_game():
    # 要有一个猜的数字
    # 要有一个用户输入的数字
    # 要对比输出结果
    target_number = 90

    while True:
        user_number = int(input("guess:"))

        if (user_number < target_number):
            print('小')
        elif (user_number > target_number):
            print('大')
        else:  # user_number == target_number
            print('OK')
            break


run_geuss_game()
