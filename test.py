# import scrapy
import requests
import re
import sys
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}
# url = 'https://www.xiashuyun.com' + chapters['url'][i].get()
url = "https://www.xiashuyun.com/227203/read_2181.html"
# c_name = chapters['title'][i].get()
# item = ChapterItem()
item = {}
item['title'] = 'c_name'
item['b_id'] = 'bnum'
item['url'] = url

# yield scrapy.Request(url, callback=self.get_chapter, headers=self.headers)
# chapter = response
chapter = etree.HTML(requests.get(url, headers=headers).text)
# //*[@id="chaptercontent"]
# 获取章节具体内容
content = chapter.xpath("//*[@id='chaptercontent']/text()")
del content[0]
if content[-2] == '\u3000\u3000':
    del content[-2]
if content[-1] == '本章未完，请点击下一页继续阅读！            ':
    del content[-1]
for i in range(len(content)):
    content[i] = str.strip(content[i])
content = '\n'.join(content)
text = content
for i in range(1, 11):
    page_num = re.search(r'read_(\d+)', url).group(1)
    page_num = 'read_' + str(page_num) + '_' + str(i)
    print(page_num)
    next_url = re.sub(r'read_(\d+)', page_num, url)
    # yield scrapy.Request(next_url, callback=self.get_chapter, headers=self.headers)
    # chapter = response
    chapter = etree.HTML(requests.get(next_url, headers=headers).text)
    content = chapter.xpath("//*[@id='chaptercontent']/text()")
    if not content:
        break
    if len(content) <= 2:
        break
    else:
        del content[0]
        if content[-2] == '\u3000\u3000':
            del content[-2]
        if content[-1] == '本章未完，请点击下一页继续阅读！            ':
            del content[-1]
        for i in range(len(content)):
            content[i] = str.strip(content[i])
        content = '\n'.join(content)
        text = text + '\n' + content
item['content'] = text

print(item)
