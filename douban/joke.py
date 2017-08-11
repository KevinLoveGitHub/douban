#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

作者：Kevin
日期：2017/5/14

"""
import scrapy


class Joke(scrapy.Item):
    info = scrapy.Field()
    director = scrapy.Field()
    country = scrapy.Field()
    type = scrapy.Field()
    year = scrapy.Field()
