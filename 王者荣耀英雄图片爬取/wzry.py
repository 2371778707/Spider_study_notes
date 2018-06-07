from urllib import  request
from urllib.request import urlretrieve
import re
import time
import os

def get_html(url):
    res = request.urlopen(url)
    html = res.read().decode('gbk')
    return html

def re_html(html):

    r1 = r'<ul class="herolist clearfix">([\s\S]*?)</ul>'
    r2 = r'<a href="([\S\s]*?)" target="_blank">'
    html = re.findall(r1,html)
    links = re.findall(r2,html[0])
    return links

def change_link(links):

        for i in range(len(links)):
            links[i] = ('http://pvp.qq.com/web201605/'+links[i])
        return links


def write_links(links):
    with open('王者荣耀英雄图片链接.txt','w',encoding='utf-8')as f:
        for link in links:
            f.write(link+'\n')
            f.flush()
        f.close()

def read_links(path):
    links = []
    with open(path,'r',encoding='utf-8')as f:
        all_link = f.read()
        f.close()
    links=all_link.split('\n')[:-1]

    return links

def get_hero_html(links):
    image_links =[]
    name_list = []

    for link in links:

        r1 = r'<div class="zk-con1 zk-con" style="background:url\(\'([\S\s]*?)\'\) center 0">'
        r2 = r'<h2 class="cover-name">([\s\S]*?)</h2>'
        res = request.urlopen(link)
        #解码
        html = res.read().decode('gbk')
        image_link_0 = 'http:'
        image_link_1 = re.findall(r1,html)
        image_link = image_link_0 + image_link_1[0]
        name = re.findall(r2,html)
        name_list.append(name[0])
        image_links.append(image_link)

    return image_links,name_list


def skin_link(image_links):

    all_image_links=[]
    skin_count = []

    for i in range(len(image_links)):


        for x in range(8):

            image_link = image_links[i][0:-5] + str(x + 1) + '.jpg'

            try:

                res = request.urlopen(image_link)

            except Exception:

                skin_count.append(x)

                break


            if res.code == 200:

                all_image_links.append(image_link)


    return  all_image_links,skin_count



def deal_filename(skin_count,name_list):

    hero_name = []

    for i in range(len(skin_count)):

        for j in range(skin_count[i]):

            hero_name.append(''.join(name_list[i])+str(j+1))

    return hero_name


def download_image(all_image_links,hero_name):

    path = os.path.join(os.getcwd(),'王者荣耀图片文件')
    if  not os.path.exists(path):

        os.mkdir(path)

    for i in range(len(all_image_links)):

        name = hero_name[i]

        print('第' + str(i + 1) + '张下载中......')

        urlretrieve(all_image_links[i], '%s.jpg' % (os.path.join(path,name)))
        print('第' + str(i + 1) + '张下载完成\n')

        if i+1 == len(all_image_links):
            print('全部下载完成！！！')


def main():

    url = 'http://pvp.qq.com/web201605/herolist.shtml'
    path = os.path.join(os.getcwd(),'王者荣耀英雄图片链接.txt')
    if  not  os.path.exists(path):
        html =  get_html(url)
        links =re_html(html)
        links = change_link(links)
        write_links(links)
    links = read_links(path)
    image_links,name_list= get_hero_html(links)
    all_image_links,skin_count = skin_link(image_links)
    hero_name = deal_filename(skin_count,name_list)
    download_image(all_image_links,hero_name)


if __name__ == '__main__':
    main()

