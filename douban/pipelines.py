# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import logging
logging.basicConfig(level=logging.ERROR)


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
    def process_item(self, item, spider):
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
