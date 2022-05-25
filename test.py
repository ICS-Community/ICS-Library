import requests
from lxml import etree

# URL = "https://www.xiashuyun.com/api/ajax/zj?id=25124&num=1663&order=asc"
URL = "https://www.xiashuyun.com/25124/read_1577.html"

req = requests.get(URL)
# 设置网页编码格式
req.encoding = 'utf8'
# 将request.content 转化为 Element
root = etree.HTML(req.content)
# 选取 ol/li/div[@class="item"] 不管它们在文档中的位置
# chapters = root.xpath("//li/a/@href")


print(chapters)