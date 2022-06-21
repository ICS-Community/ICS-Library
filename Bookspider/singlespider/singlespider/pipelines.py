import imp
from singlespider.items import NovelItem, ChapterItem

from . import settings
import pymysql

class MySQLPipeline(object):
    def __init__(self):
        self.mysql_host = settings.mysql_host
        self.mysql_user = settings.mysql_user
        self.mysql_password = settings.mysql_password
        self.mysql_db = settings.mysql_db
        self.mysql_db_charset = settings.mysql_db_charset
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.mysql_host, user=self.mysql_user, password=self.mysql_password, db=self.mysql_db, charset=self.mysql_db_charset)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):  # 插入数据
        if isinstance(item, NovelItem):
            values = (
                item['id'],
                item['name'],
                item['author'],
                item['serialstatus'],
                item['intro'],
                item['novelurl'],
            )

            sql = 'insert into book(id,name,author,serialstatus,intro,novelurl) VALUES(%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, values)
            self.conn.commit()
        elif isinstance(item, ChapterItem):
            values = (
                item['b_id'],
                item['num'],
                item['title'],
                # item['content'],
                item['url'],
            )

            sql = 'insert into chapters(b_id,num,title,url) VALUES(%s,%s,%s,%s)'
            self.cursor.execute(sql, values)
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()

import sqlite3

class SQLitePipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'tmp.db')

        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        if isinstance(item, NovelItem):
            values = (
                item['id'],
                item['name'],
                item['author'],
                item['serialstatus'],
                item['intro'],
                item['novelurl'],
            )

            sql = 'INSERT INTO books VALUES(?,?,?,?,?,?)'
            self.db_cur.execute(sql, values)
            self.db_conn.commit()
            return item
        if isinstance(item, ChapterItem):
            values = (
                item['b_id'],
                item['num'],
                item['title'],
                # item['content'],
                item['url'],
            )

            sql = 'INSERT INTO chapters VALUES(?,?,?,?)'
            self.db_cur.execute(sql, values)
            self.db_conn.commit()
            return item


# #以json格式输出
# from scrapy.exporters import JsonItemExporter
# #以jl格式输出
# #from scrapy.exporters import JsonLinesItemExporter
# #以csv格式输出
# #from scrapy.exporters import CsvItemExporter
# class SinglespiderPipeline(object):
# 	def open_spider(self, spider):
# 		#可选实现，当spider被开启时，这个方法被调用。
# 		#输出到tongcheng_pipeline.json文件
# 		self.file = open('xiashu.json', 'wb')
# 		self.exporter = JsonItemExporter(self.file, encoding='utf-8')
# 		self.exporter.start_exporting()
# 	def close_spier(self, spider):
# 		#可选实现，当spider被关闭时，这个方法被调用
# 		self.exporter.finish_exporting()
# 		self.file.close()
# 	def process_item(self, item, spider):
# 		self.exporter.export_item(item)
# 		return item