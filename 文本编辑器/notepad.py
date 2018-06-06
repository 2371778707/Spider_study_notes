# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import *
import tkinter.font as tkFont
from tkinter.messagebox import *
from tkinter import colorchooser
import re
import platform

title = "无标题"
filename=''
def new():
    content = text.get(0.0, END)
    if filename=='':
        if re.findall(r'\S', content) != []:
            back = askyesnocancel('记事本', '是否保存到' + title)
            if back == True:
                back_ = asksaveasfile(filetypes=[('文本文件','.txt')])
                try:
                    with open(back_.name,'w',encoding='utf-8')as f:
                        f.write(content)
                        f.flush()
                        f.close()
                        text.delete(0.0,END)
                        root.title(title+'-记事本')
                except Exception:
                    pass
            elif back==False:
                text.delete(0.0,END)
                root.title(title + '-记事本')
            else:
                pass
        else:
            pass
    else:
        back = askyesno('记事本','是否保存到'+filename)
        if back == True:
            content = text.get(0.0,END)
            try:
                with open(filename ,'w',encoding='utf-8')as f:
                    f.write(content)
                    f.flush()
                    f.close()
            except Exception:
                pass
        else:
            pass


def open_():
    global filename
    content = text.get(0.0, END)
    if re.findall(r'\S', content) != []:
        back = askyesnocancel('记事本', '是否保存到' + title)
        if back == True:
            back1= asksaveasfile(filetypes=[('文本文件','.txt')])

            try:
                with open(back1.name,'w',encoding='utf-8')as f:
                    f.write(content)
                    f.flush()
                    f.close()
                    text.delete(0.0,END)
            except Exception:
                pass
        elif back==False:
            text.delete(0.0,END)

        else:
            pass


    back = askopenfile(defaultextension='.txt')

    if back !=None:
        try:

            filename = back.name
            with open(back.name,'r',encoding='utf-8')as f:
              content1=f.read()
              f.flush()
              f.close()
              text.delete(0.0,END)
              text.insert(END,content1)
              root.title(back.name)
        except Exception:
            root.title(title+'-记事本')
            showerror('记事本', '无法打开文件！')
    else:
        pass


def save():

    content = text.get(0.0, END)
    if re.findall(r'\S', content) != []:
        if filename=='':
            back = askyesnocancel('记事本', '是否保存到' + title)
            if back == True:
                back_ = asksaveasfile(filetypes=[('文本文件', '.txt')])
                try:
                    with open(back_.name, 'w', encoding='utf-8')as f:
                        f.write(content)
                        f.flush()
                        f.close()
                        root.title(back_.name)
                except Exception:
                    pass
            elif back == False:
               pass
            else:
                pass
        else:
            content2 =text.get(0.0,END)
            with open(filename,'w',encoding='utf-8')as f:
                f.write(content2)
                f.flush()
                f.close()
                root.title(filename)

    else:
        showinfo('记事本','内容为空！')

def saveas():
    content = text.get(0.0, END)

    if re.findall(r'\S', content) != []:
        if filename == '':
            back = askyesnocancel('记事本', '是否保存到' + title)
            if back == True:
                back_ = asksaveasfile(filetypes=[('文本文件', '.txt')])
                try:
                    with open(back_.name, 'w', encoding='utf-8')as f:
                        f.write(content)
                        f.flush()
                        f.close()
                except Exception:
                    pass
            elif back == False:
                pass
            else:
                pass
        else:
            back_ = asksaveasfile(filetypes=[('文本文件', '.txt')])
            try:
                with open(back_.name, 'w', encoding='utf-8')as f:
                    f.write(content)
                    f.flush()
                    f.close()
            except Exception:
                pass

    else:
        showinfo('记事本', '内容为空！')

def undo():
    try:

        text.edit_undo()
    except Exception :
        showinfo(title="提示", message='已经不能上一步了！！！')
def redo():
    try:
        text.edit_redo()
    except Exception:
        showinfo(title="提示",message='已经不能下一步了！！！')
def cut():
    text.event_generate('<<Cut>>')
def copy():
    text.event_generate('<<Copy>>')

def paste():
    text.event_generate('<<Paste>>')

def quit_():
    content =text.get(1.0)
    if re.findall(r'\S', content) == []:
        sys.exit(0)
    else:

        back =askokcancel(title='记事本',message='是否保存'+title,default='ok')
        if back == True:

            w = asksaveasfile(filetypes=[('文本文件','.txt')])

        else:
            sys.exit(0)
def about():

    def okButton():
        tl.destroy()
    tl= Toplevel(root,bg='gray')
    tl.title('关于记事本')
 #   tl.iconbitmap('D:\python\Lib\idlelib\Icons\idle.ico')
    tl.geometry('600x400+400+150')
    l1=Label(tl,text=platform.platform()+'\n\n \n\n 版权：czl',bg='gray',fg='yellow')
    l1.pack(padx = 200 ,pady =80)
    btn = Button(tl,text='确定',command=okButton,width=15,height=2,bg = 'green',fg='white')
    btn.pack(padx= 200 ,pady=10)

def color():
    backcolor = colorchooser.askcolor()
    text.config(fg = backcolor[1])



def selectAll():
    content = text.get(0.0,END)
    if re.findall(r'\S', content) != []:

        text.tag_add('sel', '0.0',CURRENT)

def deleteline():
    text.config(font =ft1)

def xie():
    text.config(font = ft3)
def bold():
    text.config(font = ft4)

def underline():
    text.config(font =ft5)

root = Tk()
root.title(title+" - 记事本")
root.geometry("1000x600+300+100")
#root.iconbitmap('D:\python\Lib\idlelib\Icons\idle.ico')
toolbar = Menu(root)
root.config(menu=toolbar)
root.resizable(0,0)
fileMenu = Menu(toolbar,tearoff =0)
toolbar.add_cascade(label ='文件(F)',menu=fileMenu )
fileMenu.add_command(label='新建(N)',command=new,accelerator='Ctrl + N')
fileMenu.add_command(label='打开(O)',command=open_,accelerator='Ctrl + O')
fileMenu.add_command(label='保存(S)',command=save,accelerator='Ctrl + S')
fileMenu.add_command(label='另存为(A)',command=saveas,accelerator='Ctrl + Shift +S')
fileMenu.add_separator()
fileMenu.add_command(label='退出(Q)',command=quit_,accelerator='Ctrl + Q')
editMenu = Menu(toolbar,tearoff =0)
toolbar.add_cascade(label ='编辑(E)',menu=editMenu)

editMenu.add_command(label="上一步(Z)",command=undo,accelerator='Ctrl + Z')
editMenu.add_command(label="下一步(Y)",command=redo,accelerator='Ctrl + Y')
editMenu.add_separator()
editMenu.add_command(label="剪切(X)",command=cut,accelerator='Ctrl + X')
editMenu.add_command(label="复制(C)",command=copy,accelerator='Ctrl + C')
editMenu.add_command(label="粘贴(V)",command=paste,accelerator='Ctrl + V')
editMenu.add_command(label='全选',command = selectAll ,accelerator='Ctrl + A')
styleMenu=Menu(toolbar,tearoff =0)
toolbar.add_cascade(label="格式",menu=styleMenu)
styleMenu.add_command(label="颜色",command = color)

helpMenu=Menu(toolbar,tearoff =0)
toolbar.add_cascade(label='帮助',menu=helpMenu)
helpMenu.add_command(label='关于', command= about)

fontMenu = Menu(styleMenu,tearoff=0)
styleMenu.add_cascade(label = '字体', menu = fontMenu )
fontMenu.add_command(label='删除线',command=deleteline)
fontMenu.add_command(label='斜体',command=xie)
fontMenu.add_command(label='粗体',command=bold)
fontMenu.add_command(label='下划线',command=underline)

ft1 = tkFont.Font(family = '楷书文字',size =20 ,overstrike =1)
ft2 = tkFont.Font(family = '楷书文字',size =20 )
ft3 = tkFont.Font(family = '楷书文字',size =20,slant=tkFont.ITALIC)
ft4 = tkFont.Font(family = '楷书文字',size =20 ,weight=tkFont.BOLD)
ft5 = tkFont.Font(family = '楷书文字',size =20 ,underline = 1)

root.bind_all("<Control-n>", lambda event: new())
root.bind_all("<Control-o>", lambda event: open())
root.bind_all("<Control-s>", lambda event: save())
root.bind_all("<Control-S>", lambda event: saveas())
root.bind_all("<Control-q>", lambda event: quit_())
root.bind_all("<Control-z>", lambda event: undo())
#一般安装了搜狗输入的用不了ctrl + shift + z 有毒。。。。
root.bind_all("<Control-y>", lambda event: redo())



def _right_key(event):

    editMenu.post(event.x_root, event.y_root)

root.bind("<Button-3>", _right_key)

text =Text(root)
text.pack(fill='both',expand='yes')

scroll=Scrollbar(text)
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)
scroll.pack(side=RIGHT,fill=Y)
text.config(font =ft2)
root.mainloop()