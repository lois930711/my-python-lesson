def return_book_system():
    returned_book_namelist = []
    while True:
        returned_book_name = input("请输入你要归还的图书名称：")
        if returned_book_name == "finished":
            print("您已成功归还以下书籍", returned_book_namelist)
            break
        returned_book_namelist.append(returned_book_name)
        print("您已成功归还", returned_book_name)


return_book_system()
