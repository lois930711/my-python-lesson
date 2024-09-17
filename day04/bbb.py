# 创建一个死刑犯名单
# 提供一个签字的方法
# 什么时候执行由警察决定
# 两年后执行

def creat_name():
    name = str(input("请输入死刑犯名单"))
    print("死刑犯名单已经创建")

    def sign():
        print(name + "可以执行死刑")

    def delete():
        print(name + "废除死刑")

    return (sign, delete)


(sign, delete) = creat_name()
print("两年后")
sign()
delete()
