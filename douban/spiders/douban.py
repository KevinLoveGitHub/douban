# -*- coding: utf-8 -*-
import scrapy

from douban.items import Item


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        'https://movie.douban.com/chart',
    ]

    def parse(self, response):
        self.logger.info(response.url)
        item = Item()
        for sel in response.css('#content > div > div.article > div > div > table > tr > td:nth-child(2) > div'):
            item['title'] = sel.css('a::text').extract_first()
            item['link'] = sel.css('a::attr(href)').extract_first()
            item['pic'] = sel.css('p::text').extract_first()
            item['score'] = sel.css('div > span.rating_nums::text').extract_first()
            item['commentsNum'] = sel.css('div > span.pl::text').extract_first()
            yield item


    # def parse(self, response):
    #     item = DoubanItem()
    #     for sel in response.css('#subject_list > ul > li > div.info'):
    #         item['title']= sel.css('h2 > a::text').extract_first()
    #         item['link'] = sel.css('h2 > a::attr(href)').extract_first()
    #         item['info'] = sel.css('div.pub::text').extract_first()
    #         item['desc'] = sel.css('p::text').extract_first()
    #         yield item
