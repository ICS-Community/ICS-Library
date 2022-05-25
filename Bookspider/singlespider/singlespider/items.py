# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() # 小说名
    author = scrapy.Field() # 作者
    novelurl = scrapy.Field() # 小说地址
    serialstatus = scrapy.Field() # 状态
    serialnumber = scrapy.Field() # 连载字数
    tags = scrapy.Field() # 标签
    intro = scrapy.Field()
    pass

class ChapterItem(scrapy.Item):
    c_title = scrapy.Field()
    c_content =scrapy.Field()
    c_url = scrapy.Field()
    pass
