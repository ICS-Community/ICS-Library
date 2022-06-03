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
# 	def close_spier(selef, spider):
# 		#可选实现，当spider被关闭时，这个方法被调用
# 		self.exporter.finish_exporting()
# 		self.file.close()
# 	def process_item(self, item, spider):
# 		self.exporter.export_item(item)
# 		return item


import sqlite3


class Sqlite3Pipeline(object):

    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get(
                'SQLITE_FILE'),  # 从 settings.py 提取
            sqlite_table=crawler.settings.get('SQLITE_TABLE', 'items')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        insert_sql = "insert into {0}({1}) values ({2})".format(self.sqlite_table,
                                                                ', '.join(
                                                                    item.fields.keys()),
                                                                ', '.join(['?'] * len(item.fields.keys())))
        self.cur.execute(insert_sql, item.fields.values())
        self.conn.commit()

        return item
