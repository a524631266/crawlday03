#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/28 0:18
"""

import requests
from bs4 import BeautifulSoup


url="http://w3school.com.cn/"
url2="http://www.jsiq.net/hs.php?srchmem=&page=1"

response=requests.get(url)
# response.encoding="gb2312"
print(response.encoding)
print(response.request.headers)

# soup=BeautifulSoup(response.text,"lxml")
soup=BeautifulSoup(response.content,"lxml")
print soup
#如果还出现编码问题，需要在header中添加两块语言方面的字典
#head={'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'zh-CN,zh;q=0.8'}
if __name__=='__main__':
        "http://w3school.com.cn/"