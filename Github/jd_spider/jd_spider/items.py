# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class goodsItem(scrapy.Item):
    link = scrapy.Field()  # 商品链接
    ID = scrapy.Field()  # 商品ID
    name = scrapy.Field()  # 商品名字
    comment_num = scrapy.Field()  # 评论人数
    shop_name = scrapy.Field()  # 店家名字
    price = scrapy.Field()  # 价钱
    commentVersion = scrapy.Field()  # 为了得到评论的地址需要该字段
    score1count = scrapy.Field()  # 评分为1星的人数
    score2count = scrapy.Field()  # 评分为2星的人数
    score3count = scrapy.Field()  # 评分为3星的人数
    score4count = scrapy.Field()  # 评分为4星的人数
    score5count = scrapy.Field()  # 评分为5星的人数


class commentItem(scrapy.Item):
    user_name = scrapy.Field()  # 评论用户的名字
    user_ID = scrapy.Field()  # 评论用户的ID
    userProvince = scrapy.Field()  # 评论用户来自的地区
    content = scrapy.Field()  # 评论内容
    good_ID = scrapy.Field()  # 评论的商品ID
    good_name = scrapy.Field()  # 评论的商品名字
    date = scrapy.Field()  # 评论时间
    replyCount = scrapy.Field()  # 回复数
    score = scrapy.Field()  # 评分
    status = scrapy.Field()  # 状态
    title = scrapy.Field()
    userLevelId = scrapy.Field()
    userRegisterTime = scrapy.Field()  # 用户注册时间
    productColor = scrapy.Field()  # 商品颜色
    productSize = scrapy.Field()  # 商品大小
    userLevelName = scrapy.Field()  # 银牌会员，钻石会员等
    userClientShow = scrapy.Field()  # 来自什么 比如来自京东客户端
    isMobile = scrapy.Field()  # 是否来自手机
    days = scrapy.Field()  # 天数
    commentTags = scrapy.Field()  # 标签
