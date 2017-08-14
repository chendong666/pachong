# -*- coding: utf-8 -*-
# python_version:2.7.13
# 获取北京今明后三天天气

import urllib2
from bs4 import BeautifulSoup
import lxml.etree as etree


# 面向过程
# url='http://jinan.tianqi.com/15/'
# a=urllib2.urlopen(url).read()
# soup=BeautifulSoup(a,'html.parser')
# b=soup.find_all('div',class_="table_day15")
# for c in b[0:3]:
#     print c.get_text()
# x =raw_input('  ')

# 面向对象

# 使用bs4
class Weather(object):
    def __init__(self, urls):
        self.url = urls
        self.soup = 'a'
        self.text = []

    def get_soup(self):
        a = urllib2.urlopen(self.url).read()
        self.soup = BeautifulSoup(a, 'html.parser')
        # 安装了lxml模块的可以将html.parser改为lxml，速度会稍快

    def get_text(self):
        b = []
        bb = self.soup.find_all('div', class_="table_day15")
        for bbb in bb:
            b.append(bbb.get_text())
        self.text = b[0:3]

    def xian_shi(self):
        for c in self.text:
            print c


def main(urls):
    a = Weather(urls)
    a.get_soup()
    a.get_text()
    a.xian_shi()



# xpath
# 继承Weather类
class Weather2(Weather):
    def __init__(self, urls):
        super(Weather2,self).__init__(urls)

    def get_tree(self):
        a = urllib2.urlopen(self.url).read()
        self.tree = etree.HTML(a)
        # 安装了lxml模块的可以将html.parser改为lxml，速度会稍快

    def get_text(self):
        bb = self.tree.xpath('//div[@class="table_day15"]')
        self.text = bb[0:3]

    def xian_shi(self):
        for c in self.text:
            print c.xpath('string()')


def main2(urls):
    a = Weather2(urls)
    a.get_tree()
    a.get_text()
    a.xian_shi()
if __name__ == '__main__':
    # 地址的http:/+地名的拼音.tianqi.com/15/即可改为其他地方
    url = 'http://beijing.tianqi.com/15/'
    main(url)
    print '使用xpath解析器'
    main2(url)
