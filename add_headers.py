#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/27 23:04
"""
import requests
from bs4 import  BeautifulSoup

def test_webpage(url):
    #一般会根据服务器的要求添加识别标记
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"lxml")
    # text=soup.select("#article_details > div.article_title > h1 > span > a")

    # print(text)
    print(response.status_code)#403
    print(response.request.headers)#{'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.11.1'}  python开头
    print(soup.head.title.text)

if __name__=='__main__':
    # test_webpage("http://blog.csdn.net/wswzjdez/article/details/5694942")
    test_webpage("http://www.cec.com.cn")