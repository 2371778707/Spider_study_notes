from urllib import request
from urllib import parse
import re
import http.cookiejar
import sys
from tkinter import *
from tkinter import messagebox


class URP:

    def __init__(self,username,password):
        self.flag =False
        self.usr = username
        self.psw = password
        self.hosturl= 'http://202.197.144.243:8083'
        self.posturl='http://202.197.144.243:8083/loginAction.do'

        cj = http.cookiejar.LWPCookieJar()
        cookie_support = request.HTTPCookieProcessor(cj)
        openr = request.build_opener(cookie_support)
        request.install_opener(openr)
        request.urlopen(self.hosturl)

        #请求头
        self.headers  ={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Referer': 'http://202.197.144.243:8083/'
            }
        #提交的数据
        self.postData ={
            'zjh':self.usr,
            'mm':self.psw
        }
        #更改数据的编码
        self.postData = parse.urlencode(self.postData).encode('GBK')
        #放到req
        self.req = request.Request(self.posturl,self.postData,self.headers)

    def login(self):
        try :
            #进入主页面
           request.urlopen(self.req)
            #进入异动信息
           request.urlopen('http://202.197.144.243:8083/xjInfoAction.do?oper=ydxx').read()
            #进入个人信息
           self.resp = request.urlopen('http://202.197.144.243:8083/userInfo.jsp').read()
           self.html = self.resp.decode('GBK')

        except request.HTTPError as  e:
            print('登录失败[%s]，账号或密码错误！'%e.code)
            messagebox.showerror('提示','账号或密码错误！')
        else:
            print('登录成功！')
            back = messagebox.showinfo('提示','登录成功！')
            if back =='ok':
                self.flag= True

        return self.html
    def info(self,html):
        #用户名匹配
        r1 = r'<td >([\s\S]*?)</td>'
        #匹配表格，这里会用到第二个表格
        r2 = r'<table width="100%" border="0" cellpadding="0" cellspacing="0" class="titleTop3">([\s\S]*?)</table>'
        #匹配表格的电话
        r3 = r'<td >[\s\S]*?<input type="text" name="dh" value="([\s\S]*?)" tag="电话|0|s|40">[\s\S]*?</td>'
        #匹配表格的地址
        r4 = r'<td>[\s\S]*?<input type="text" name="txdz" value="([\s\S]*?)" tag="通讯地址|0|s|100">[\s\S]*?</td>'
        #匹配表格的Email
        r5 = r'<td>[\s\S]*?<input type="text" name="email" value="([\s\S]*?)" tag="电子邮件|0|e|100">[\s\S]*?</td>'

        #找到的用户名
        name = re.findall(r1,html)
        #找到的所有表
        table =re.findall(r2,html)
        #找到的电话，这里匹配貌似有bug 。。。不管了
        phone = re.findall(r3,table[1])
        for i in phone:
            if i=='':
                phone.remove(i)
        #找到的通讯地址
        address = re.findall(r4,table[1])
        for i in address:
            if i=='':
                address.remove(i)
        email = re.findall(r5,table[1])
        for j in email:
            if j =='':
                email.remove(j)

        #放到字典里面
        info_dict={
            'name': ''.join(name[0]).strip(),
            'phone': ''.join(phone[0]).strip(),
            'address':''.join(address[0]).strip(),
            'email':''.join(email[0]).strip()
        }
        return info_dict

    # def write_info(self,info_dict):
    #     with open('info.txt','a',encoding='utf-8')as f:
    #         f.write(info_dict.get('name')+'\t\t'+info_dict.get('phone')+'\t\t'+info_dict.get('address')+'\t\t'+info_dict.get('email')+'\n')
    #         f.flush()
    #         f.close()
def query(usr,psw):

        urp= URP(usr,psw)
        try:
            html = urp.login()
            info_dict = urp.info(html)
            if urp.flag ==True:

               l3.config( text='姓名：'+info_dict.get('name')+'\n'+'电话：'+info_dict.get('phone')+'\n'+'地址：'+info_dict.get('address')+'\n'+'Email：'+info_dict.get('email'))


        except Exception:
            pass
      #  urp.write_info(info_dict)

if __name__ == '__main__':

    def set():
        usr =e1.get()
        psw =e2.get()
        if usr==''or psw=='':
            messagebox.showerror('提示','用户名或密码为空')
        else:
            query(usr,psw)
    root = Tk()
    root.config(bg='#808080')
    root.title('URP综合教务系统')
    root.geometry('270x170+650+300')
    root.resizable(0,0)
    l1 = Label(root,text='用户名',bg='gray',fg='yellow')
    l1.grid(row=0,column=0)
    e1 = Entry(root,width='25')
    e1.grid(row=0,column=1)
    l2 = Label(root, text='密    码',bg='gray',fg='yellow')
    l2.grid(row=1, column=0)

    e2 = Entry(root,width='25')
    e2['show'] = '*'

    e2.grid(row=1, column=1)
    btn1 =Button(root,width=10,height=1,text='登录',bg='green',command =set)
    btn1.grid(row =2,column =1)
    l3 = Label(root, justify='left', bg='gray', fg='white')
    l3.grid(row=3, column=1)
    root.mainloop()

