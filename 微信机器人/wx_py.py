from wxpy import *
import sys
def printSuccess():
    print('登录成功！'+'你使用的是'+str(sys.platform)+'平台登录！')

def printExit():
    print('微信Web退出登录！')

bot = Bot(cache_path=True,login_callback=printSuccess,logout_callback=printExit)

#查找所有的朋友
fris = bot.friends()

#定义数组
fris_list=[]

#遍历朋友姓名，放到列表里面
for fri in fris:
    fris_list.append(fri.name)

#遍历列表给每一个朋友发信息
for i in range(len(fris_list)):
    #根据姓名找到那个人,可能有同名的，这里只要第一个
    fri_ = bot.friends().search(fris_list[i])[0]

    #如果想过滤。。谁。。可以 判断一下，人比较多的时候 ，可以放到列表里面 遍历发送 ！！！！
    if fris_list[i] == '妈妈':
        fri_.send("在忙吗？")
    else:
        fri_.send("群发程序测试！！！不要回复！！！！")

print('群发消息发送成功！')

#打印一下发给谁了 ，这里要根据具体 你写的代码。。。看你过滤了谁  。。
for fri in fris:


   print('已发送好友：'+fri.name)



bot.logout()








