from urllib import request
import re
import os
class 虎牙直播王者荣耀人气排名:

    网址="http://www.huya.com/g/2336"
    正则匹配规则='<span class="txt">([\s\S]*?)</li>'
    主播名字匹配规则='<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
    主播人气匹配规则='<i class="js-num">([\s\S]*?)</i>'
    def __获取网页源码(self):
       请求返回的字节码= request.urlopen(self.网址)
       网页=请求返回的字节码.read()
       网页=str(网页,encoding='utf-8')
       return  网页

    def __正则匹配(self,网页):
       匹配数据= re.findall(self.正则匹配规则,网页)
       return 匹配数据

    def __整理一下(self,匹配数据):


        所有主播=[]
        for 数据 in 匹配数据:

           主播名字=re.findall(self.主播名字匹配规则,数据)
           主播人气=re.findall(self.主播人气匹配规则,数据)
           某个主播={'主播名字':主播名字,'主播人气':主播人气}
           所有主播.append(某个主播)
        return 所有主播

    def __格式整理(self,所有主播):
        格式=lambda 某个主播:{
            '主播名字':某个主播['主播名字'][0].strip(),
            '主播人气':某个主播['主播人气'][0]
        }
        return map(格式,所有主播)

    def __排行(self,所有主播):

        所有主播=sorted(所有主播,key=self.__人气排行,reverse=True)
        return 所有主播

    def __人气排行(self,所有主播):

        人气=re.findall('\d*',所有主播['主播人气'])
        人气=float(人气[0])
        if '万' in 所有主播['主播人气']:
            人气*=10000
        return 人气

    def __显示(self,所有主播):
        for 某个主播 in 所有主播:
            print(某个主播['主播名字']+'--------------'+某个主播['主播人气'])

    def 进入(self):
        print("虎牙直播直播平台《王者荣耀》主播人气实时排行：")
        网页=self.__获取网页源码()
        匹配数据=self.__正则匹配(网页)
        所有主播=self.__整理一下(匹配数据)
        所有主播=list(self.__格式整理(所有主播))
        所有主播=self.__排行(所有主播)
        self.__显示(所有主播)

while True:

    os.system('clear')

    虎牙直播王者荣耀人气排名().进入()