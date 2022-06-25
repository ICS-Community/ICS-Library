

from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class BookTemplate():
    id = Column(Integer, primary_key=True)  # 主键自增
    name = Column(String(100))
    author = Column(String(100))
    serialstatus = Column(String(100))
    intro = Column(String(100))
    novelurl = Column(String(100))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])


class ChapterTemplate():
    b_id = Column(Integer, primary_key=True)  # 主键自增
    num = Column(String(100))
    title = Column(String(100))
    content = Column(String(100))
    url = Column(String(100))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])


class DownNovelSpidersPipeline(object):

    def __init__(self):  # 执行爬虫时
        self.engine = create_engine('mysql://root:@localhost:3306/novels?charset=utf8', echo=True)  # 连接数据库
        self.session = sessionmaker(bind=self.engine)
        self.sess = self.session()
        Base = declarative_base()
        # 动态创建orm类,必须继承Base, 这个表名是固定的,如果需要为每个爬虫创建一个表,请使用process_item中的
        self.Book = type('Books', (Base, BookTemplate),
                         {'__tablename__': 'books'})
        self.Chapter = type('Chapters', (Base, ChapterTemplate), {
                            '__tablename__': 'chapters'})

    def process_item(self):  # 爬取过程中执行的函数
        # 按照爬虫名动态创建一个类
        # if not hasattr(self,spider.name):
        #     self.Article = type(spider.name, (Base, ArticleTemplate), {'__tablename__': spider.name, })
        # 在数据库中创建这个表
        # if spider.name not in self.engine.table_names(): #create table for this spider
        self.Book.metadata.create_all(self.engine)
        self.Chapter.metadata.create_all(self.engine)
        # if isinstance(item, NovelItem):
        #     self.sess.add(self.Book(**item))
        #     self.sess.commit()
        # elif isinstance(item, ChapterItem):
        #     self.sess.add(self.Chapter(**item))
        #     self.sess.commit()

    def close_spider(self, spider):  # 关闭爬虫时
        self.sess.close()

DownNovelSpidersPipeline()
DownNovelSpidersPipeline().process_item()