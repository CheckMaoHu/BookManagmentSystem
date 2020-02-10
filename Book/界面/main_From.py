#主界面选择界面 增删改查界面 分为两个界面
#管理员界面
#用户界面
import Operation.inquire_Operator as Inquire
import Operation.book_Operator as Book
import Operation.user_Operator as User
def mainAdminFrom(str):
    while(True):
        print("--------------------欢迎%s-------------------"%(str[1]))
        print("                  系统主界面")
        print("书籍查询[1]\t书籍管理[2]\t用户管理[3]\t返回上一级[4]\t")
        print("--------------------欢迎%s-------------------" % (str[1]))
        print("请输入上面数字")
        m=int(input())
        if(m==1):
            Inquire.inquire(str)
        elif(m==2):
            Book.bookManagement(str)
        elif(m==3):
            User.userManagement(str)
        elif(m==4):
            break
        else:
            print("无效指令，请再次输入")
def mainUserFrom(str):
    while(True):
        print("---------------欢迎%s------------------" % (str[1]))
        print("             系统主界面")
        print("书籍查询[1]\t用户管理[2]\t返回上一级[3]\t")
        print("---------------欢迎%s------------------" % (str[1]))
        print("请输入上面数字")
        m = int(input())
        if (m == 1):
            Inquire.inquire(str)
        elif (m == 2):
            User.userManagement(str)
        elif(m==3):
            break
        else:
            print("无效指令，请再次输入")
