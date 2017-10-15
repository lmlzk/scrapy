# -*- coding: utf-8 -*-
import scrapy

from myspider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['[http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath('//div[@class="li_txt"]')
        # data_list = []
        for node in node_list:
            item = MyspiderItem()
            item['name'] = node.xpath('./h3/text()').extract_first().strip()
            item['title'] = node.xpath('./h4/text()').extract_first().strip()
            item['desc'] = node.xpath('./p/text()').extract_first().strip()

            yield item
            # data_list.append(item)
        # return data_list


