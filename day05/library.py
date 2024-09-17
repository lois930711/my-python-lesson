# 实现一个还书系统
# 用数组来表示已经归还的书名
# while 来循环
# 使用 input 方法来要求用户输入书名
# 注意点：如果用户输入的字符串是：finished
# 就停止还书流程
# 停止后，print 输出：你已经归还一下书：把上面的数组输出一下


def return_book_system():
    # 第一步 []
    # return_book_totallist = None
    return_book_totallist = []
    # ??
    system_end_word = "finished"

    while True:
        # 期望用户输入的是书名，例如："我们仨"
        return_book_list = str(input("请输入本次归还的书籍名称："))
        print('line1:', return_book_list)
        return_book_totallist = return_book_totallist, return_book_list
        print('line2:', return_book_totallist)
        return_book_totallist_print = list[return_book_totallist]
        print('line3:', return_book_totallist_print)
        if return_book_list == system_end_word:
            print("你已经归还一下书：", return_book_totallist_print)
            break


return_book_system()
