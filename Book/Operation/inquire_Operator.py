#主要是查找函数，用来查找书籍
#精确查找与模糊查找  两个关键字够了，不然太繁琐
#暂时是分模块，需要待会加入循环
book=[["数据结构","严","1"],["数据库","胡","2"],["张宇18讲","张宇","3"],["线代讲义","李永乐","4"],["其他","胡","5"]]
def inquire(str):
    while(True):
        print("精确[1]\t模糊[2]\t返回上一级[3]\t")
        l=int(input())
        if(l==1):
            print("请输入书名：  作者：  ")
            bookName = input()
            bookAnuthor = input()
            for i in book:
               if(i[0]==bookName and i[1]==bookAnuthor):
                   print("查询到  书名:" + i[0] + "  作者:" + i[1] + "  ISBN号:" + i[2])
                   break
            else:
                 print("没有找到该书籍")
        elif(l==2):
            print("请输入书名：  作者：  ")
            flag=False
            bookName = input()
            bookAnuthor = input()
            for i in book:
              if((bookName in i[0] and bookName!="") or  (bookAnuthor in i[1])and bookAnuthor!=""):
                  print("查询到  书名:" + i[0] + "  作者:" + i[1] + "  ISBN号:" + i[2])
                  flag=True
            if(not flag):
             print("没有查询到书籍")
        elif(l==3):
            break
        else:
            print("无效指令，请再次输入")



