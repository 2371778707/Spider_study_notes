import string
import re
from urllib import  request

class Html_Tool:

    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    # 用非 贪婪模式 匹配 任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")
    #  用非 贪婪模式 匹配 任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")
    replaceTab=[("<","<"),(">",">"),("&","&"),("&","\""),("","")]

    def Replace_Char(self,x):
        x=str(x)
        x=self.BgnCharToNoneRex.sub('',x)
        x=self.BgnPartRex.sub('\n    ',x)
        x=self.CharToNewLineRex.sub('\n',x)
        x=self.CharToNextTabRex.sub('\t',x)
        x=self.EndCharToNoneRex.sub('',x)
        for t in self.replaceTab:
            x = x.replace(t[0],t[1])
        return x
class Baidu_Spider:
    def __init__(self,url):
        self.myUrl =url
        self.datas=[]
        self.myTool=Html_Tool()
        print('已经启动百度贴吧爬虫,咔擦咔擦')

    def baidu_tieba(self):

        myPage =request.urlopen(self.myUrl).read().decode('utf-8')
        endPage=self.page_counter(myPage)
        title =self.find_title(myPage)
        print("标题："+title)
        self.save_data(self.myUrl,title,endPage)

    def page_counter(self,myPage):

        list1=re.findall(r'<span class="red">(\d*)</span>\s*?页',myPage,re.S)
        if list1[0]!=0:
            endPage = int(list1[0])
            print("评论共有%d页"%(endPage))
        else:
            endPage=0
            print("无法计算！")
        return endPage;

    def find_title(self,myPage):

        myMatch = re.search(r'<h1.*?>(.*?)</h1>', myPage, re.S)
        title = '标题'

        if myMatch:
            title = myMatch.group(1)
        else:
            print('无法获取标题！')
            # 文件名不能包含以下字符： \ / ： * ? " < > |
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')

        return title # 用来存储楼主发布的内容

    def save_data(self,url,title,endPage):
         # 加载页面数据到数组中
         self.get_data(url,endPage)
         # 打开本地文件
         f = open(title+'.txt','w+',encoding='utf-8')
         f.writelines(self.datas)
         f.close()
         print ('文件已下载到本地并打包成txt文件')
         # 获取页面源码并将其存储到数组中
    def get_data(self,url,endPage):
        url = url + '?pn='
        for i in range(1,endPage+1):
            print('爬虫%d号正在加载中...' % i )
            myPage = request.urlopen(url + str(i)).read().decode('utf-8')
            # 将myPage中的html代码处理并存储到datas里面
            self.deal_data(myPage)


    # 将内容从页面代码中抠出来
    def deal_data(self,myPage):

        myItems = re.findall('id="post_content.*?>(.*?)</div>',myPage,re.S)
        for item in myItems:
            data = self.myTool.Replace_Char(item.replace("\n",""))


            self.datas.append(data+'\n')

bdurl =input("请输入贴吧网址：")

mySpider = Baidu_Spider(bdurl)
mySpider.baidu_tieba()
