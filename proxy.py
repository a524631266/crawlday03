#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/27 23:55
"""

#www.xicidaili.com
#http://www.kuaidaili.com/
#because of the free of ip proxy ,so some of the proxy ips are not stable
#so you can test the stability of the ip that you have caught using a def.
import requests
from bs4 import BeautifulSoup

def get_proxy_ip(url):
    proxys={'http':'139.217.12.225:80'}
    response=requests.get(url,proxies=proxys)
    soup=BeautifulSoup(response.text,"lxml")
    # print(soup)
    fp=soup.select("body > p")[0].text
    print(fp)


if __name__=='__main__':
    get_proxy_ip('http://icanhazip.com/')