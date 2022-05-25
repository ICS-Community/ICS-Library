import scrapy
from Novel.items import NovelItem
import re
from copy import deepcopy
import urllib
import copy
class DownnovelSpider(scrapy.Spider):
    name = 'DownNovel'
    allowed_domains = ['www.qu.la']
    start_urls = ['https://www.qu.la/book/1230/']
    #div_list = response.xpath("//div[@class='article']/div[@class='']/div[@class='']")
    current_page = 1  #设置当前页

    def parse(self, response):
        item = NovelItem()
        #现获取当前页的所有章节
        chapter_list = response.xpath("//div[@class='section-box']/ul[@class='section-list fix']")[1]
        chapters = chapter_list.xpath('./li')
        item['current_page'] = self.current_page
        #遍历当前所有章节
        for chapter_id,chapter in enumerate(chapters):
            # chapter 是用来后面进行排序的
            item['chapter_url']=chapter.xpath("./a/@href").extract_first()
            item['chapter_name'] = chapter.xpath("./a/text()").extract_first()
            item['chapter_url'] ='http://www.qu.la'+ item['chapter_url']
            yield scrapy.Request(
                url=item['chapter_url'],
                callback=self.parse_chapter,
                meta={'item':deepcopy(item)},
                cb_kwargs={'num': chapter_id + 1}
            )
        # 下一页
        next_url=response.xpath("//div[@class='listpage']/span[@class='right']/a/@href").extract_first()
        next_url = urllib.parse.urljoin(response.url,next_url)
        # if next_url != 'https://www.qu.la/book/1230/index_3.html':
        #     self.current_page+=1
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        # 
        #     )
        if next_url !=response.url:
            self.current_page+=1
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_chapter(self,response,num):
        item = response.meta['item']
        # item['num'] = str(chapter_id) + ':'
        item['num']=num
        print(item['num'])
        item['chapter_title'] = response.xpath("//div[@class='reader-main']/h1/text()").extract_first()
        item['chapter_content'] = response.xpath("//div[@class='content']/text()").extract()
        item['chapter_content'] = [i.strip() for i in item['chapter_content'] if item['chapter_content']!='' ]
        chapter_content = ''.join(item['chapter_content'])
        item['chapter_content'] = re.sub("'',", '', chapter_content)
        yield item