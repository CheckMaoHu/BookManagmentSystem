#操作函数
#主要是管理员登录和普通会员登录，识别登录的账号
adminList=[["admin","123456"],["admin1","123456"]]
basisList=[["hu","123"],["hh","1234"]]
def loginOper(user,psw):

    flag=False
    for i in adminList:
        if(user==i[0] and psw==i[1]):
            print("管理登录成功")
            Admin="Admin"
            return user,Admin
        else:flag=True
    for j in basisList:
        if (user == j[0] and psw == j[1]):
            print("用户登录成功")
            User="User"
            return user,User
        else:
            flag = True
    if(flag==True):
        print("登录失败")
        return False,False
#注册函数
def register(user,psw):
    ISexist=False
    for i in basisList:
        if(user==i[0]):
            print("用户名已存在")
            ISexist=True
            break
    for j in adminList:
        if(user==j[0]):
            print("用户名已存在")
            ISexist=True
            break
    if(not ISexist):
        basisList.append([user,psw])
        print("注册成功")
    return ISexist






