from urllib.request import *
import re
import os
import music_link

r1 = r'<p id="lrcName">([\s\S]*?)</p>'

r2 = r'<div id="llrcId" style="overflow-x: hidden;overflow-y: hidden;">[\s\S]*?([\s\S]*?)</div>'

music_link.link()

path = os.path.join(os.getcwd(),"音乐地址.txt")

path1 = os.path.join(os.getcwd(), '歌词')



with open(path,'r',encoding='utf-8') as f:
    music_link_str=f.read()
    f.close()

music_link_list =music_link_str.split('\n')

#去掉最后一个空。。字符


music_link_list = music_link_list[0:len(music_link_list)-1]


for i in range(len(music_link_list)):

    music_lrc = []

    res = urlopen(str(music_link_list[i]).strip())

    html = res.read().decode('utf-8')

    result1 =re.findall(r1,html)

    result2 =re.findall(r2,html)

    print('第'+str(i+1)+'首歌词下载完成！')

    try :

        list1 = result2[0].split('>')
    except Exception :
        print("对不起，网络错误！请重新运行！")

    for  a  in range(len(list1)):

         if a%2==0 :
             pass
         else:
             list2 = list1[a].split('<')
             music_lrc.append(list2[0])



    if not os.path.exists(path1):

       os.mkdir(path1)
       # 处理名字中有/的
    include_ = ''.join(result1[0]).split('/')

    if len(include_) == 0:

        with open(path1+'/'+''.join(result1[0])+'.txt','w') as f:


              for music in music_lrc:

                 f.write(''.join(music)+'\n')

              f.close()

    else:

        with open(path1+'/'+''.join(include_)+'.txt','w') as f:

            for music in music_lrc:

                f.write(''.join(music) + '\n')

            f.close()

