import requests
import re
import sys
from lxml import etree

url = 'https://www.xiashuyun.com/227203/read_2181_3.html'
chapter = etree.HTML(requests.get(url).text)
content = chapter.xpath("//*[@id='chaptercontent']/text()")