# -*- coding: utf-8 -*-
import scrapy
from douban.movie import Movie


class DoubanMovieSpider(scrapy.Spider):
    name = "doubanMovie"

    allowed_domains = ["douban.com"]

    # 自定义设置请求头信息
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/event-stream',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,zh-HK;q=0.2',
        },

        'USER_AGENT':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/57.0.2987.133 Safari/537.36 ',

        'ITEM_PIPELINES': {
            'douban.pipelines.DoubanPipeline': 300,
            'douban.pipelines.LeanCloudPipeline': 300
        }
    }

    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        item = Movie()
        for sel in response.xpath('//div[@class="item"]'):
            item['title'] = sel.xpath('div/a/img/@alt').extract_first()
            item['pic'] = sel.xpath('div/a/img/@src').extract_first()
            item['link'] = sel.xpath('div/a/@href').extract_first()
            item['info'] = sel.xpath('div[2]/div[2]/p[2]/span/text()').extract_first()
            item['score'] = sel.xpath('div[2]/div[2]/div/span[2]/text()').extract_first()
            item['commentsNum'] = sel.xpath('div[2]/div[2]/div/span[4]/text()').re(r'\d+')[0]
            item['director'] = sel.xpath('div[2]/div[2]/p/text()').re(r'导演: (.*?)\s')[0]
            item['year'] = sel.xpath('div[2]/div[2]/p/text()[2]').re(r'([0-9]+)')[0]
            country_type = sel.xpath('div[2]/div[2]/p/text()[2]').re(r'\xa0/\xa0(.*)\xa0/\xa0(.*)')
            item['country'] = country_type
            item['country'] = country_type[0]
            item['type'] = country_type[1]
            yield item

        next_line = response.xpath('//span[@class="next"]/a/@href').extract_first()

        if next_line:
            yield scrapy.Request(response.urljoin(next_line), self.parse)


