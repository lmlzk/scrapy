# -*- coding: utf-8 -*-
import scrapy

from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']
    host = 'http://hr.tencent.com/'

    def parse(self, response):
        response.selector.remove_namespaces()
        test = response.css(".even")
        name = test.xpath('./td[1]/a/text()').extract()
        print("*"*30,len(name))
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for node in node_list:
            item = TencentItem()
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['link'] = self.host + node_list.xpath('./td[1]/a/@href').extract_first()
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['time'] = node.xpath('./td[5]/text()').extract_first()

            # yield item
            yield scrapy.Request(item['link'], callback=self.parse_detail, meta={'key':item})

        next_url = self.host + response.xpath('//*[@id="next"]/@href').extract_first()
        yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['key']
        item['duty'] = response.xpath('//tr[3]/td/ul/li/text()').extract_first().strip()
        item['require'] = response.xpath('//tr[4]/td/ul/li/text()').extract_first().strip()

        yield item

