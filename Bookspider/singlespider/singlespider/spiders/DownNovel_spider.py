import re
import scrapy
from ..items import *
# from copy import deepcopy
# import urllib
# import copy

class DownnovelSpider(scrapy.Spider):
    name = 'DownNovel'
    # allowed_domains = ['www.qu.la']
    '''
    下书网的构造方法
    https://www.xiashuyun.com/type/nan_0_0_allvisit_7.html
    https://www.xiashuyun.com/type/nan_0_0_allvisit_5.html
    https://www.xiashuyun.com/type/nv_0_0_allvisit_1.html

    "//div[@id="waterfall"]/div[@class='item']"
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.xiashuyun.com/type/nan_0_0_allvisit_1.html'
        yield scrapy.Request(url, headers=self.headers)
    
    #div_list = response.xpath("//div[@class='article']/div[@class='']/div[@class='']")
    # current_page = 1  #设置当前页

    def parse(self, response):
        # 获取当前页面的所有书籍
        books = response.xpath("//div[@id='waterfall']/div[@class='item']")
        if books:
            for book in books:
                book_num = book.xpath("div[@class='title']/h3/a/@href")
                bookurl = "https://www.xiashuyun.com" + book_num
                yield scrapy.Request(bookurl, callback=self.getBooks, cb_kwargs={'bnum': book_num}, headers=self.headers)
                pass
            # 下一页
            # 如果books存在数据则对下一页进行采集
            page_num = re.search(r'allvisit_(\d+)', response.url).group(1)
            page_num = 'allvisit_' + str(int(page_num)+1)
            next_url = re.sub(r'allvisit_\d+', page_num, response.url)
            yield scrapy.Request(next_url, headers=self.headers)

    def getBook(self, response, bnum):
        book = response
        item = NovelItem()
        item['name'] = book.xpath("//div[@id='info']/div[@class='infotitle']/h1/text()")[0]
        author = book.xpath("div[@class='pic']/div/text()")[0]
        author = re.sub(r' /.*', '', author)
        item['author'] = author
        item['novelurl'] = response.url
        item['serialstatus'] = book.xpath("//div[@id='info']/div[@class='infotitle']/span/text()")[0]
        # item['serialnumber'] =  # 没有字数统计
        intor = '\n'.join(book.xpath("//div[@id='info']/div[@id='aboutbook']/text()"))
        intor = re.sub(r'\u3000\u3000', '', intor)
        item['intro'] = intor
        cnum = book.xpath("//*[@id='mainright']/div[1]/ul/li[2]/text()")[0]
        cnum = int(re.search(r'\d+', cnum).group(0))
        chapters_url = 'https://www.xiashuyun.com/api/ajax/zj?id=' + bnum + '&num=' + cnum + '&order=asc'
        yield scrapy.Request(chapters_url, callback=self.get_chapter_list, headers=self.headers)

    def get_chapter_list(self, response):
        response.body.decode('utf-8')
        clist = response
        chapters = clist.xpath("//li/a/@href")
        for chapter in chapters:
            """
            构成
            read_1577.html
            read_1577_3.html
            请求，如果为空，返回本章已爬取完毕，如果book_id相同，就合并章节。
            """
            url = 'https://www.xiashuyun.com' + chapter
            yield scrapy.Request(url, callback=self.get_chapter, headers=self.headers, cb_kwargs={'bnum': book_num})

    def get_chapter(self, response):
        chapter = response
        item = ChapterItem()
        item['c_title'] = chapter.xpath("/html/body/section/div/article/div[1]/h1/a/text()")
        content = chapter.xpath("//*[@id='chaptercontent']")









        #现获取当前页的所有章节
       
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




            