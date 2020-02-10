#修改用户名
#修改密码
import Operation.admin_Operator as static1
def userManagement(successful):
    while(True):
        print("修改密码[1]\t返回上一级[2]\t")
        accept=int(input())
        flag=False
        if(accept==1):
            print("请输入旧密码:")
            oldPsw=input()
            print("请输入新密码:")
            newpsw=input()
            for i in static1.adminList:
                if (successful[0] == i[0] and oldPsw == i[1]):
                    i[1]=newpsw
                    print("修改成功")
                    flag = True
                    break

            for j in static1.basisList:
                if (successful[0] == j[0] and oldPsw == j[1]):
                    j[1] = newpsw
                    print("修改成功")
                    flag = True
                    break

            if(not flag):
                print("原密码错误")
        elif(accept==2):
            break
        else:
            print("无效指令，请再次输入")