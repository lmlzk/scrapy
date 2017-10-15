# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Sun.items import SunItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    rules = (
        Rule(LinkExtractor(allow=r'questionType'), follow=True),
        Rule(LinkExtractor(allow=r'http://wz.sun0769.com/html/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = SunItem()

        item['number'] = response.xpath('//div[@class="ctitle"]/div[1]/strong/text()').extract_first().split(':')[-1].strip()
        item['url'] = response.url
        item['title'] = response.xpath('/html/head/title/text()').extract_first().split('_')[0]

        content = response.xpath('/html/body/div[6]/div/div[2]/div[1]//text()').extract()
        data = ''.join([con.strip() for con in content])

        item['content'] = data

        yield item