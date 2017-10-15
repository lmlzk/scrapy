# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from myspider.items import MyspiderItem


class Itcast2Spider(CrawlSpider):
    name = 'itcast2'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    rules = (
        Rule(LinkExtractor(allow=r'channel/teacher'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        node_list = response.xpath('//div[@class="li_txt"]')
        # data_list = []
        for node in node_list:
            item = MyspiderItem()
            item['name'] = node.xpath('./h3/text()').extract_first().strip()
            item['title'] = node.xpath('./h4/text()').extract_first().strip()
            item['desc'] = node.xpath('./p/text()').extract_first().strip()

            yield item
