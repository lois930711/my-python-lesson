

# 打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (j, i, i*j), end=" ")
#     print()
# print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------)


def 九九乘法表():
    # 定义被乘数为行数
    for a in range(1, 10):
        乘法表每行 = ""
        # 定义乘数为被乘数+1
        for b in range(1, a+1):
            c = a * b
            乘法表每行 = 乘法表每行 + str(b) + "x" + str(a) + "=" + str(c) + " "
        print(乘法表每行)


九九乘法表()
