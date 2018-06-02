import urllib.request
import re
res=urllib.request.urlopen("http://www.kuwo.cn/bang/index")
html=res.read().decode('utf-8')

print(html)
