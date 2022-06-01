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
        # Print("开始新的一页")
        books = response.xpath("//div[@id='waterfall']/div[@class='item']").getall()
        if books:
            for book in books:
                book_num = book.xpath("div[@class='title']/h3/a/@href").get()
                bookurl = "https://www.xiashuyun.com" + str(book_num)
                yield scrapy.Request(bookurl, callback=self.getBook, cb_kwargs={'bnum': book_num}, headers=self.headers)
                pass
            # 下一页
            # 如果books存在数据则对下一页进行采集
            page_num = re.search(r'allvisit_(\d+)', response.url).group(1)
            page_num = 'allvisit_' + str(int(page_num)+1)
            next_url = re.sub(r'allvisit_\d+', page_num, response.url)
            yield scrapy.Request(next_url, headers=self.headers)

    def getBook(self, response, bnum):
        # print("开始爬取第"+ bnum+"号书籍")
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
        yield item
        cnum = book.xpath("//*[@id='mainright']/div[1]/ul/li[2]/text()")[0]
        cnum = int(re.search(r'\d+', cnum).group(0))
        chapters_url = 'https://www.xiashuyun.com/api/ajax/zj?id=' + bnum + '&num=' + cnum + '&order=asc'
        yield scrapy.Request(chapters_url, meta={'cnum': cnum, 'bnum': bunm}, callback=self.get_chapter, headers=self.headers)

    def get_chapter(self, response):
        response.body.decode('utf-8')
        clist = response
        cnum = clist.meta['cnum']
        bnum = clist.meta['bnum']
        chapters = {}
        chapters['url'] = clist.xpath("//li/a/@href")
        chapters['title'] = clist.xpath("//li/a/text()")
        for i in range(cnum):
            """
            构成
            read_1577.html
            read_1577_3.html
            请求，如果为空，返回本章已爬取完毕，如果book_id相同，就合并章节。
            """
            url = 'https://www.xiashuyun.com' + chapters['url'][i]
            c_name = chapters['title'][i]

            yield scrapy.Request(url, callback=self.get_chapter, headers=self.headers)

            #//*[@id="chaptercontent"]
            # 获取章节具体内容
            chapter = response
            item = ChapterItem()
            item['title'] = c_name
            item['b_id'] = bnum
            item['url'] = url
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
                page_num = 'read_' + str(int(page_num)) + '_' + i
                next_url = re.sub(r'read_\d+', page_num, url)
                yield scrapy.Request(url, callback=self.get_chapter, headers=self.headers)
                chapter = response
                content = chapter.xpath("//*[@id='chaptercontent']/text()")
                if len(content) == 0 :
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
            yield item