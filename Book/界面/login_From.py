#管理员 账号 admin  123456
#普通用户 账号 注册即可
import Operation.admin_Operator as adminOp
import 界面.main_From as mainFrom
#这是所有的登录界面
while(True):
    # print("【注：本程序为输入一行，回车一次，勿怪】")
    print("------------------------")
    print("\t图书管理系统登录")
    print("登录[1]\t注册[2]\t退出[3]")
    print("------------------------")
    print("请输入数字")
    lo = int(input())
    if(lo==1):
        print("请输入用户名:______密码：______")
        user=input()
        psw=input()
        successful=adminOp.loginOper(user,psw)
        if(successful[1]=="Admin"):
            mainFrom.mainAdminFrom(successful)
        elif successful[1]=="User":
            mainFrom.mainUserFrom(successful)
        else:
            print("用户名或者密码错误")
    elif(lo==2):
        print("请输入用户名：______密码：______")
        user = input()
        psw = input()
        adminOp.register(user,psw)
    elif(lo==3):
        break
    else:
        print("请再次选择")


