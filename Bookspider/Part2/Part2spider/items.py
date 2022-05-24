# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 电影名称
    book_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    start1 = scrapy.Field()
    
    # 评论人数
    score_num = scrapy.Field()
