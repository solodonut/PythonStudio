# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import mysql
import mysql.connector
from mysql.connector import pooling
from mysql.connector import errorcode
from scrapy.utils.project import get_project_settings

SETTINGS = get_project_settings()


class MySQLPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        # 初始化数据库信息
        dbconfig = {
            'user': SETTINGS['DB_USER'],
            'password': SETTINGS['DB_PASSWD'],
            'host': SETTINGS['DB_HOST'],
            'port': SETTINGS['DB_PORT'],
            'database': SETTINGS['DB_DB'],
            'charset': 'utf8',
            'raise_on_warnings': True
        }

        # 创建连接池
        self.conn_pool = pooling.MySQLConnectionPool(pool_name=SETTINGS['POOL_NAME'],
                                                               pool_size=SETTINGS['POOL_SIZE'],
                                                               pool_reset_session=True,
                                                               **dbconfig)

    def process_item(self, item, spider):

        try:
            # 从连接池创建链接
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()

            # 插入商品信息Insert语句
            add_goods = ("INSERT INTO jd_goods \
                          (ID, name, comment_num, shop_name, link, commentVersion, \
                            score1count, score2count, score3count, score4count, score5count, price) \
                          VALUES (%(ID)s, %(name)s, %(comment_num)s, %(shop_name)s, %(link)s, \
                            %(commentVersion)s, %(score1count)s, %(score2count)s, %(score3count)s, \
                            %(score4count)s, %(score5count)s, %(price)s)")

            # 插入的数据值
            data_goods = {
                'ID': item['ID'][0],
                'name': item['name'][0],
                'comment_num': str (item['comment_num']),
                'shop_name': item['shop_name'][0],
                'link': item['link'][0],
                'commentVersion': str(item['commentVersion'])[1:-1],
                'score1count': str(item['score1count']),
                'score2count': str(item['score2count']),
                'score3count': str(item['score3count']),
                'score4count': str(item['score4count']),
                'score5count': str(item['score5count']),
                'price': str(item['price']),
            }

            # 执行SQL语句
            cursor.execute(add_goods, data_goods)

            # Make sure data is committed to the database
            conn.commit()
            cursor.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("=======")
                print(err)
        finally:
            conn.close()

        return item


class CommentPipeline(object):
    pass