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
            links[i] = ('http://pvp.qq.com/web201605/'+links[i]+'\n')
        return links

def get_hero_html(links):
    image_links =[]
    for link in links:

        r1 = r'<div class="zk-con1 zk-con" style="background:url\(\'([\S\s]*?)\'\) center 0">'
        res = request.urlopen(link)
        #解码
        html = res.read().decode('gbk')
        image_link_0 = 'http:'
        image_link_1 = re.findall(r1,html)
        image_link = image_link_0 + image_link_1[0]

        image_links.append(image_link)

    return image_links

def download_image(image_links):

    path = os.path.join(os.getcwd(),'王者荣耀图片文件')
    if  not os.path.exists(path):

        os.mkdir(path)

    for i in range(len(image_links)):

        time.sleep(0.5)
        urlretrieve(image_links[i],'%s.jpg' %  (os.path.join(path,'第'+str(i+1)+'张图')))

        print('第'+str(i+1)+'张图片正在下载中......')

        if i+1 == len(image_links):

            print('下载完成！！！')




def main():

    url = 'http://pvp.qq.com/web201605/herolist.shtml'
    html =  get_html(url)
    links =re_html(html)
    links = change_link(links)
    image_links = get_hero_html(links)
    download_image(image_links)

if __name__ == '__main__':
    main()

