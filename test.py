# import scrapy
import requests
import re
import sys
from lxml import etree

#  selector = etree.HTML(sourceHtml)

def get_t():
    url='https://www.xiashuyun.com/246825/read_152.html'
    url2 = "https://www.xiashuyun.com/api/ajax/zj?id=246825&num=2413&order=asc"
    # r = scrapy.Request(url) 
    r = requests.get(url)

    f = open("a.html", 'w')
    f.write(r.text)
    f.close()

    r = requests.get(url2)
    # r.encoding='gbk' 
    f = open("b.html", 'w')
    f.write(r.text)
    f.close()

def aa():
    sourceHtml = open("b.html" , 'r')
    sourceHtml = sourceHtml.read()
    # print(sourceHtml)
    r = etree.HTML(sourceHtml)
    chapters = {}
    chapters['url'] = r.xpath("//li/a/@href")
    chapters['title'] = r.xpath("//li/a/text()")
    # print(r[0].href)
    cnum = len(chapters['url'])
    for i in range(cnum):
            """
            构成
            read_1577.html
            read_1577_3.html
            请求，如果为空，返回本章已爬取完毕，如果book_id相同，就合并章节。
            """
            url = 'https://www.xiashuyun.com' + chapters['url'][i]
            c_name = chapters['title'][i]
            print(url)
            print(c_name + ": " + url)

# get_t()

sourceHtml = open("a.html" , 'r')
sourceHtml = sourceHtml.read()
# print(sourceHtml)
r = etree.HTML(sourceHtml)

content = r.xpath("//*[@id='chaptercontent']/text()")
del content[0]
if content[-2] == '\u3000\u3000':
    del content[-2]
if content[-1] == '本章未完，请点击下一页继续阅读！            ':
    del content[-1]
for i in range(len(content)):
    content[i] = str.strip(content[i])
    # print(t)
content = '\n'.join(content)
f = open("b.txt", 'w')
f.write(content)
f.close()

