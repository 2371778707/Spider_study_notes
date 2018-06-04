import urllib.request
import re

def link():

    res=urllib.request.urlopen("http://www.kuwo.cn/bang/index")
    html=res.read().decode('utf-8')

    #网页源码只有一个<ul></ul>标签  ？可用可不用
    r1 = r'<ul class="listMusic">[\s\S]*</ul>'
    r2 = r'<div class="name">[\s\S]*?</div>'
    r3 = r'<a href="([\s\S]*)" target="_blank">[\s\S]*</a>'

    #只会返回一个，列表长度为1
    result1 = re.findall(r1,html)
    #非贪婪模式
    result2= re.findall(r2,result1[0])

    result3 = []

    for i in range(len(result2)):

        result3.append(re.findall(r3,result2[i]))

    with open('音乐地址.txt','w',encoding='utf-8') as f:

        for i in range(len(result3)):

            f.write(''.join(result3[i])+'\n')

        f.close()


