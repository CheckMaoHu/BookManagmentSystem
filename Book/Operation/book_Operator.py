#管理员的书籍操作
#增，改,删
import Operation.inquire_Operator as Book
# import 界面.main_From as MainFrom
#写个while循环选择界面
import os
def bookManagement(str):
    while(True):
        print("-------------------书籍操作界面------------------")
        print("增加书籍[1]\t修改书籍[2]\t删除书籍[3]\t返回主界面[4]")
        print("-------------------书籍操作界面------------------")
        print("输入上述操作选择")
        b=int(input())
        if(b==1):
            # 获取需要的书籍，资料
            print("输入需要添加的书名:_______作者:_______ISBN号:_______")
            bookName=input()
            bookAuthor=input()
            bookIsbn=input()
            # def addBook(bookName,bookAuthor,bookIsbn): 算了这儿不调用函数了
            Book.book.append([bookName,bookAuthor,bookIsbn])
            print(Book.book)
            print("录入成功")
        elif(b==2):
            #获取需要修改的书籍
            print("输入需要修改的书名：")
            oldBookName = input()
            # def updateBook():
            for i in Book.book:
                print("输入要修改的书名:_______作者:_______ISBN号:_______")
                bookName = input()
                bookAuthor = input()
                bookIsbn = input()
                if i[0]==oldBookName:
                    i[0]=bookName
                    i[1]=bookAuthor
                    i[2]=bookIsbn
                    print(Book.book)
                    print("修改成功")
                    break
            else:
                print("没有该书籍存在")
        elif(b==3):
            #获取需要删除的书籍
            print("输入要删除的书名:_______作者:_______ISBN号:_______")
            bookName = input()
            bookAuthor = input()
            bookIsbn = input()
            for i in Book.book:
                if (i[0]==bookName and i[1]==bookAuthor):
                    Book.book.remove(i)
                    print(Book.book)
                    print("删除成功")
        elif(b==4):
            break
        else:
           print("无效指令，请再次输入")







