# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://www.lagou.com/jobs/list_python']

    def parse(self, response):
        print(response.body.decode())
        node_list = response.xpath('//*[@id="s_position_list"]/ul/li/div[@class="list_item_top"]')
        node_li_len = len(node_list)
        print("===============",node_li_len)
