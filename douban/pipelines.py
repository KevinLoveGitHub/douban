# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import logging
import leancloud

logging.basicConfig(level=logging.DEBUG)


def dbHandle():
    conn = pymysql.connect(
        host='45.76.79.73',
        user='root',
        db='douban',
        password='xiaoguang',
        charset='utf8',
        use_unicode=False,
    )
    return conn


class DoubanPipeline(object):
    @staticmethod
    def process_item(item, spider):
        db = dbHandle()
        cursor = db.cursor()
        sql = 'INSERT INTO movie (title, info, director, pic, link, score, commentsNum, country, type, year)' \
              ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        try:
            cursor.execute(sql, (item['title'], item['info'], item['director'], item['pic'], item['link'],
                                 item['score'], item['commentsNum'], item['country'], item['type'], item['year']))
            db.commit()
        except Exception as e:
            logging.error(e)
            db.rollback()

        return item


class LeanCloudPipeline(object):
    @staticmethod
    def process_item(item, spider):
        leancloud.init("JBCyid797qS5I6OfT45DP1zM-gzGzoHsz", "q3wI59KSKaPcdnTtebtuJnog")
        movie = leancloud.Object.extend('Movie')
        test_object = movie()
        test_object.set('title', item['title'])
        test_object.set('info', item['info'])
        test_object.set('director', item['director'])
        test_object.set('pic', item['pic'])
        test_object.set('link', item['link'])
        test_object.set('score', item['score'])
        test_object.set('commentsNum', item['commentsNum'])
        test_object.set('country', item['country'])
        test_object.set('type', item['type'])
        test_object.set('year', item['year'])
        test_object.save()
