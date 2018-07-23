from urllib.request import *
import re
import os
# 导入歌词链接
import music_link

r1 = r'<p id="lrcName">([\s\S]*?)</p>'
r2 = r'<div id="llrcId" style="overflow-x: hidden;overflow-y: hidden;">[\s\S]*?([\s\S]*?)</div>'
# 调用link（）

music_link.link()

path = os.path.join(os.getcwd(), "音乐地址.txt")

path1 = os.path.join(os.getcwd(), '歌词')

with open(path, 'r', encoding='utf-8') as f:
    music_link_str = f.read()
    f.close()

music_link_list = music_link_str.split('\n')

music_link_list = music_link_list[0:len(music_link_list) - 1]


for i in range(len(music_link_list)):

    music_lrc = []

    res = urlopen(str(music_link_list[i]).strip())

    html = res.read().decode('utf-8')

    result1 = re.findall(r1, html)

    result2 = re.findall(r2, html)

    if result1 == []:

        pass

    else:
        print("歌曲名称：" + result1[0])
        try:
            list1 = result2[0].split('>')

        except Exception:

            pass

        for a in range(len(list1)):

            if a % 2 == 0:
                pass
            else:

                list2 = list1[a].split('<')
                music_lrc.append(list2[0])

        if not os.path.exists(path1):

            os.mkdir(path1)

            # 处理名字中有/，|，\\的

        IrlName = ''.join(result1[0]).replace("/", "-")

        IrlName1 = IrlName.replace("|", "-")

        IrlName2 = IrlName1.replace("\\", "-")

        with open(path1 + '/' + IrlName2 + '.txt', 'w', encoding="utf-8") as f:
            try:
                f.write(IrlName2 + '\n')
                for music in music_lrc:
                    f.write(music + '\n')
                f.close()
            except:
                pass