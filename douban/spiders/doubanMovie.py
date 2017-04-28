# -*- coding: utf-8 -*-
import scrapy

from douban.movie import Movie
import re


class DoubanMovieSpider(scrapy.Spider):
    name = "doubanMovie"
    allowed_domains = ["douban.com"]
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        item = Movie()
        response.sdfjklsjdflsjkflksdjfklsfj()
        for sel in response.xpath('//*[@id="content"]/div/div[1]/ol/li/div'):
            item['title'] = sel.xpath('div/a/img/@alt').extract_first()
            item['pic'] = sel.xpath('div/a/img/@src').extract_first()
            item['link'] = sel.xpath('div/a/@href').extract_first()
            item['info'] = sel.xpath('div[2]/div[2]/p[2]/span/text()').extract_first()
            item['score'] = sel.xpath('div[2]/div[2]/div/span[2]/text()').extract_first()
            item['commentsNum'] = sel.xpath('div[2]/div[2]/div/span[4]/text()').extract_first()
            item['commentsNum'] = re.match('[0-9]+', item['commentsNum']).group()
            yield item
