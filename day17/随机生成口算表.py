
import random
# 随机生成n以内的口算表


def 口算表(n: int):

    符号 = ["+", "-", "*", "/"]
    # n为需要生成的题数
    for a in range(1, n+1):
        第一个数 = random.randint(1, n+1)
        题目 = ""
        第二个数 = random.randint(1, n+1)
        随机符号 = random.choice(符号)
        题目 = 题目 + str(第一个数) + str(随机符号) + str(第二个数) + "=" + "  "
        if 第一个数+第二个数 > 100 or 第一个数*第二个数 > 100:
            pass
        else:
            print(题目)


def 加法(num1: tuple[int, int], num2: tuple[int, int], n: int = 25):
    result_list = []

    while True:
        if len(result_list) == n:
            break

        随机数1 = random.randint(num1[0], num1[1]+1)
        随机数2 = random.randint(num2[0], num2[1]+1)
        if 随机数1+随机数2 > 100:
            pass
        else:
            算数 = str(随机数1)+"+"+str(随机数2)+"="
            result_list.append(算数)

    return result_list


result_加法 = 加法((1, 100), (1, 100), 10)
print(result_加法)


def 减法(num1: tuple[int, int], num2: tuple[int, int], n: int = 25):
    result_list = []

    while True:
        if len(result_list) == n:
            break
        随机数1 = random.randint(num1[0], num1[1]+1)
        随机数2 = random.randint(num2[0], num2[1]+1)
        if 随机数1-随机数2 < 0:
            pass
        else:
            算数 = str(随机数1)+"-"+str(随机数2)+"="
            result_list.append(算数)

    return result_list


result_减法 = 减法((1, 100), (1, 100), 10)
print(result_减法)
