# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from douban.joke import Joke


class QiubaiSpider(CrawlSpider):
    name = "qiubai"
    allowed_domains = ["qiushibaike.com"]

    # 自定义设置请求头信息
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,zh-HK;q=0.2',
        },

        'USER_AGENT':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/58.0.3029.110 Safari/537.36',
    }

    start_urls = ['http://www.qiushibaike.com/']

    rules = (
        Rule(LinkExtractor(allow='joke/[0-9]+'), callback='parse_item', follow=True),
    )

    @staticmethod
    def parse_item(response):
        item = Joke()
        item['info'] = response.url
        yield item
