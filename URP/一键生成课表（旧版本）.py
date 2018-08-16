from urllib import request
from urllib import parse
import re
import http.cookiejar
from collections import OrderedDict
from pyexcel_xls import save_data
from tkinter import *
from tkinter import messagebox
import os
import csv
import getpass
class URP:


    def makeexcelfile(self,path, data):
        dic = OrderedDict()
        for sheetName, sheetValue in data.items():
            d = {}
            d[sheetName] = sheetValue
            dic.update(d)
        save_data(path, dic)

    def __init__(self,username,password):
        self.usr = username
        self.psw = password
        self.all_row =[]

        self.hosturl= 'http://202.197.144.243:8083'
        self.posturl =  'http://202.197.144.243:8083/loginAction.do'
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
           self.resp = request.urlopen('http://202.197.144.243:8083/xkAction.do?actionType=6').read()
           self.html = self.resp.decode('GBK')

        except request.HTTPError as  e:
            print('登录失败!')
            messagebox.showerror('提示','登录失败，用户名或密码错误！')
            return None
        else:
            print('登录成功！')
            back= messagebox.askyesno('提取','登录成功！\n是否提取课表？')
            if back==True:
                return self.html

    def get_Table(self,html):
        r1 = r'<table cellpadding="0" width="100%" class="displayTag" cellspacing="1" border="0" id="user">([\s\S]*?)</table>'
        r2 = r'<td[\s\S]*?>([\S\s]*?)</td>'
        table_list = re.findall(r1,html)
        td_list=re.findall(r2,table_list[0])
        for i in  range(len(td_list)):
               td_list[i]= ''.join(td_list[i]).replace('\r','')
               td_list[i]= ''.join(td_list[i]).replace('\n','')
               td_list[i] =''.join(td_list[i]).replace('\t','')
               td_list[i] =''.join(td_list[i]).replace('&nbsp;','')
               td_list[i] =''.join(td_list[i]).replace('<br>','')
               td_list[i] =''.join(td_list[i]).replace('<div align="center">','')
               td_list[i] =''.join(td_list[i]).replace('</div>','')
               td_list[i] =''.join(td_list[i]).replace('<p class="style4">','')
               td_list[i] = ''.join(td_list[i]).replace('</p>', '')
               td_list[i] = ''.join(td_list[i]).replace('<p align="center" class="td2 style5"><strong>', '')
               td_list[i] = ''.join(td_list[i]).replace('</strong>', '').strip()

        return td_list


    def write_file(self,td_list):
        with open('C:/Users/'+getpass.getuser()+'/Desktop/课表.txt','w',encoding='utf-8')as f:
          f.write(''+'|')
          for i in range(len(td_list)):

            if i<8:
                f.write(td_list[i]+'|')
            elif i==8:
                f.write('\n'+td_list[8]+'|')
            elif i>8 and i<17:
                f.write(td_list[i]+'|')
            elif i==17:
                f.write('\n'+''+'|'+td_list[17]+'|')
            elif i>17 and i<25:
                f.write(td_list[i]+'|')
            elif i==25 :
                f.write('\n' + '' + '|' + td_list[25] + '|')
            elif i>25 and  i<33:
                f.write(td_list[i]+'|')
            elif i==33:
                f.write('\n' + '' + '|' + td_list[33] + '|')
            elif i>33 and i<41:
                f.write(td_list[i]+'|')
            elif i==41:
                f.write('\n'+ td_list[41] +'|'+'\n')
            elif i>41 and i<51:
                f.write(td_list[i]+'|')
            elif i==51:
                f.write('\n' + '' + '|' + td_list[51] + '|')
            elif i>51 and i<59:
                f.write(td_list[i]+'|')
            elif i==59:
                f.write('\n' + '' + '|' + td_list[59] + '|')
            elif i>59 and i<67:
                f.write(td_list[i]+'|')
            elif i ==67:
                f.write('\n' + '' + '|' + td_list[67] + '|')
            elif i>67 and i<75:
                f.write(td_list[i]+'|')
            elif i==75:
                f.write('\n' + td_list[75] + '|' + '\n')
            elif i>75 and i<85:
                f.write(td_list[i]+'|')
            elif i==85:
                f.write('\n' + '' + '|' + td_list[85] + '|')
            elif i>85 and i<94:
                f.write(td_list[i]+'|')
          f.flush()
          f.close()

    def read_file(self):
        with open('C:/Users/'+getpass.getuser()+'/Desktop/课表.txt','r',encoding='utf-8') as f:
            content = f.read()
            rows = content.split('\n')
        f.close()
        f=open('C:/Users/'+getpass.getuser()+'/Desktop/课表.csv','w',encoding='gb18030',newline='')

        writer = csv.writer(f,dialect='excel')
        for row in rows:
            row = row.split('|')[0:-1]
            writer.writerow(row)
        f.flush()
        f.close()
def query(usr,psw):

        urp= URP(usr,psw)
        html = urp.login()
        if html ==None:
            pass
        else:
            td_list = urp.get_Table(html)
            urp.write_file(td_list)
            urp.read_file()
            os.remove('C:/Users/'+getpass.getuser()+'/Desktop/课表.txt')
            messagebox.showinfo('提示','课表提取成功！在桌面上"课表.csv文件"')

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
    root.title('一键提取课表')
    root.geometry('270x150+650+300')
    root.resizable(0,0)
    l1 = Label(root,text='用户名',bg='gray',fg='yellow',height=2)
    l1.grid(row=0,column=0)
    e1 = Entry(root,width='25')
    e1.grid(row=0,column=1)
    l2 = Label(root, text='密    码',bg='gray',fg='yellow',height=2)
    l2.grid(row=1, column=0)
    e2 = Entry(root,width='25')
    e2['show'] = '*'
    e2.grid(row=1, column=1)
    btn1 =Button(root,width=10,height=1,text='登录并提取',bg='green',fg='white',command =set)
    btn1.grid(row =2,column =1)
    l3 = Label(root, justify='left', bg='gray', fg='white')
    l3.grid(row=3, column=1)
    root.mainloop()

