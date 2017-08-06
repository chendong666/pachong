# -*- coding: utf-8 -*-
# __author__='wukong'
# python_version:2.7.13
#获取北京今明后三天天气
import urllib2
from bs4 import BeautifulSoup
class huoqutianqi():
    def __init__(self, url):
        self.url = url
        self.soup = 'a'
        self.text = []
    def getsoup(self):
        a = urllib2.urlopen(self.url).read()
        self.soup = BeautifulSoup(a,'html.parser')
    def gettext(self):
        b=[]
        bb=self.soup.find_all('div',class_="table_day15")
        for bbb in bb:
            b.append(bbb.get_text())
        self.text=b[0:3]
    def xianshi(self):
        for c in self.text:
            print c
def main(url):
    a= huoqutianqi(url)
    a.getsoup()
    a.gettext()
    a.xianshi()
        
if __name__ ==  '__main__':
    #地址的http:/+地名的拼音.tianqi.com/15/即可改为其他地方
    url='http://beijing.tianqi.com/15/'
    main(url)
x =raw_input('  ')
