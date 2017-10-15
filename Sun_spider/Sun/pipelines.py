# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.conf import settings
# 导入pymongo模块用于操作mongodb数据库
from pymongo import MongoClient

class SunPipeline(object):
    def __init__(self):
        # 创建存储数据的文件
        self.file = open('dongguan.json','w')

    def process_item(self, item, spider):
        # 转换成字典，再转换成字符串
        result = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        # 将数据写入文件
        self.file.write(result)
        return item

    def close_spider(self, spider):
        # 关闭存储数据的文件
        self.file.close()


class MongoPipleline(object):
    def __init__(self):
        # 读取配置参数
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        colname = settings['MONGO_COLNAME']

        # 链接mongodb数据库
        self.handle = MongoClient(host,port)

        # 选择数据库
        self.db = self.handle[dbname]

        # 选择集合
        self.col = self.db[colname]

    def process_item(self, item, spider):
        # 将item实例转化成字典
        data = dict(item)

        # 写入数据库
        self.col.insert(data)

        # 返回item
        return item



    def close_spider(self, spider):
        # 关闭数据库链接
        self.handle.close()













