# -*- coding: utf-8 -*-
import scrapy
import re
import json
from jd_spider.items import goodsItem
from scrapy.selector import Selector


class JdGoodsSpider(scrapy.Spider):
    name = "jd_goods"
    start_urls = []

    for i in range(1, 85):  # 这里请自己设置页数，目前只抓取手机下前85页的商品
        url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
        start_urls.append(url)

    # 第一个执行的函数，爬取start_urls列表中的网址
    def parse(self, response):  # 解析搜索页
        sel = Selector(response)  # Xpath选择器

        goods = sel.xpath('//li[@class="gl-item"]')  # 粗略获取商品信息
        for good in goods:
            item = goodsItem()
            item['ID'] = good.xpath('./div/@data-sku').extract()
            item['name'] = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            item['shop_name'] = good.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract()
            item['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()
            url = "http:" + item['link'][0] + "#comments-list"

            # 生成新的Request请求商品详细页面，获取更多商品相关信息，通过回调函数执行parse_detail

            yield scrapy.Request(url, meta={'item': item}, callback=self.parse_detail)

    # 被parse函数调用，获取商品详细页面里的信息
    def parse_detail(self, response):
        item = response.meta['item']  # 从parse函数通过meta参数传过来

        # 默认返回的response.body为bytes格式需要转换成str
        response_body =response.body.decode('utf-8', 'ignore')

        # 通过commentVersion: 将HTML页面分割成两半，后半部分开头几个字符(10个内)为所需要的ID
        temp = response_body.split('commentVersion:')

        pattern = re.compile("[\'](\d+)[\']")

        if len(temp) < 2:  # 如果没有找到commentVersion:说明无评论则设为 -1
            item['commentVersion'] = -1
        else:
            match = pattern.match(temp[1][:10])
            item['commentVersion'] = match.group()

        url = "http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds=" + str(item['ID'][0])

        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_getcommentnum)

    def parse_getcommentnum(self, response):

        item = response.meta['item']

        # response.body是一个json格式的
        js = json.loads(response.body.decode('utf-8', 'ignore'))
        item['score1count'] = js['CommentsCount'][0]['Score1Count']
        item['score2count'] = js['CommentsCount'][0]['Score2Count']
        item['score3count'] = js['CommentsCount'][0]['Score3Count']
        item['score4count'] = js['CommentsCount'][0]['Score4Count']
        item['score5count'] = js['CommentsCount'][0]['Score5Count']
        item['comment_num'] = js['CommentsCount'][0]['CommentCount']
        item_id = item['ID'][0]  # 获得商品ID
        url = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + item_id + "&origin=2"

        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_price)

    def parse_price(self, response):

        item = response.meta['item']

        # 默认返回的response.body为bytes格式需要转换成str
        response_body = response.body.decode('utf-8', 'ignore')
        temp = response_body.split('jQuery([')
        s = temp[1][:-4]  # 获取到需要的json内容
        js = json.loads(str(s))  # js是一个list

        if 'pcp' in js:  # dict.has_key()方法 在3.X版本之后停止使用
            item['price'] = js['pcp']
        else:
            item['price'] = js['p']
        return item