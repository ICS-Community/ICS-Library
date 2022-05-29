import scrapy
import requests

url='https://www.xiashuyun.com/type/nan_0_0_allvisit_1.html'
r = scrapy.Request(url) 
rq = requests.get(url)

f = open("a.html", 'w')

# f.write(r.text)

f.close()