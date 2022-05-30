#以json格式输出
from scrapy.exporters import JsonItemExporter
#以jl格式输出
#from scrapy.exporters import JsonLinesItemExporter
#以csv格式输出
#from scrapy.exporters import CsvItemExporter
class SinglespiderPipeline(object):
	def open_spider(self, spider):
		#可选实现，当spider被开启时，这个方法被调用。
		#输出到tongcheng_pipeline.json文件
		self.file = open('xiashu.json', 'wb')
		self.exporter = JsonItemExporter(self.file, encoding='utf-8')
		self.exporter.start_exporting()
	def close_spier(selef, spider):
		#可选实现，当spider被关闭时，这个方法被调用
		self.exporter.finish_exporting()
		self.file.close()
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item