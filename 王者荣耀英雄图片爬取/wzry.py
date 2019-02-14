from urllib import  request
from  urllib.request import urlretrieve
import os,json

def get_html(url):
    res = request.urlopen(url)
    html = res.read().decode('utf8')
    html =html.encode('utf8')[3:].decode('utf8')
    html = html.replace("&#10;","")
    #print(html)
    return html

def get_hero_list(html):
    hero = json.loads(html)
    #print(hero)
    return  hero
def get_ImgIconUrl(hero):
    Icon_url=[]
    for i in enumerate(hero):
        ename = i[1]["ename"]
        url = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + str(ename) + "/" + str(ename) + ".jpg"
        Icon_url.append(url)
       # print(url)
    return Icon_url

def makeFile():
    path = os.path.join(os.getcwd(), '王者荣耀图片文件')
    if not os.path.exists(path):
        os.mkdir(path)
        _type = ["战士", "法师", "坦克", "刺客", "射手", "辅助"]
        for i in  range(len(_type)):
            os.mkdir(path+"/"+_type[i])
    return path

def makeFileIcon():
    path = os.path.join(os.getcwd(), '王者荣耀图片文件Icon')
    if not os.path.exists(path):
        os.mkdir(path)
    return path
def get_hero_name(hero):
    hero_name=[]
    for i in enumerate(hero):
        cname = i[1]["cname"]
        hero_name.append(cname)
    return hero_name

def download_image(Iconurl,name,pathIcon):
    for i in range(len(Iconurl)):
        urlretrieve(Iconurl[i],"%s.jpg"%(pathIcon+"/"+name[i]))
        print("正在下载"+name[i]+"...")

def get_hero_type(hero_type):
    _type = ["战士", "法师", "坦克", "刺客", "射手", "辅助"]
    return _type[hero_type-1]


def get_skin_name(hero):
    skin_Name = []
    for i in enumerate(hero):
        skin_name = i[1]["skin_name"]
        skin_Name.append(skin_name)
    #print(skin_Name)
    return skin_Name

def get_skin_num(skin_name):
    sname = []
    snum = []
    for i in  range(len(skin_name)):
        skins = skin_name[i]
        who = skins.split("|")
        sname.append(who)
        snum.append(len(who))
    return  sname,snum

def download_Img(hero,name,sname,snum,path):
    for  i in range(len(hero)):
        ename = hero[i]["ename"]
        for j in range(snum[i]):
            url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+str(ename)+"/"+str(ename)+"-bigskin-"+str(j+1)+".jpg"
           # print(url)
            urlretrieve(url,"%s.jpg"%(path+"/"+get_hero_type(hero[i]["hero_type"])+"/"+sname[i][j]))
            print("正在下载"+sname[i][j]+".jpg ...")
        print(name[i]+"英雄图片下载...结束\n")

def main():
    url = "https://pvp.qq.com/web201605/js/herolist.json"
    html = get_html(url)
    hero = get_hero_list(html)
    Icon_url = get_ImgIconUrl(hero)
    pathIcon = makeFileIcon()
    path = makeFile()
    name = get_hero_name(hero)
    #下载头像图标
    download_image(Icon_url,name,pathIcon)
    skin_name = get_skin_name(hero)
    sname,snum =get_skin_num(skin_name)
    #下载大图片
    download_Img(hero,name,sname,snum,path)






if __name__ == '__main__':
    main()