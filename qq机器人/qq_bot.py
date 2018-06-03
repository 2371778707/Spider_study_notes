from  qqbot import _bot as bot

#输入自己QQ
bot.Login(['-q','2371778707'])

#更新好友列表
bot.Update('buddy')

#获取所有好友
friends = bot.List('buddy')
#定义空列表
friend_list = []

#判断好友列表是否为空
if not friends == []:

    #遍历好友
    for friend in friends:

        #将好友姓名加入列表中
        friend_list.append(friend.name)

    for i in range(len(friend_list)):

        friend_ = bot.List('buddy', friend_list[i])[0]

        if  friend_list[i] == "新伤":


             content1 = "机器人测试！！！！！！！！！！！"

             content2 = "在吗？"

             bot.SendTo(friend_,content1,resendOn1202 = True)

        else:

            pass

            # bot.SendTo(friend_,content2,resendOn1202 = True)