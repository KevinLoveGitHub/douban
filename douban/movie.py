#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

作者：Kevin
日期：2017/4/27

"""
import scrapy
from douban.items import Item


class Movie(Item):
    info = scrapy.Field()
    direct = scrapy.Field()
    star = scrapy.Field()
