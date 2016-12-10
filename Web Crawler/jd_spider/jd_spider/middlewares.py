# coding=utf-8

import random
import base64
from jd_spider.settings import PROXIES
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


# 主要用来动态获取user agent, user agent列表USER_AGENTS在setting.py中进行配置
class RandomUserAgent(UserAgentMiddleware):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        print(crawler.settings.getlist('USER_AGENTS'))
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))

# 用来切换代理，proxy列表PROXIES也是在settings.py中进行配置
class ProxyMiddleware(object):
    def process_request(self, request, spider):

        proxy = random.choice(PROXIES)

        if proxy['user_pass'] is not None:

            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.b64encode(proxy['user_pass'].encode(encoding='utf-8'))
            request.headers['Proxy-Authorization'] = 'Basic ' + str(encoded_user_pass)
            print("**************ProxyMiddleware have pass************" + proxy['ip_port'])
        else:
            print("**************ProxyMiddleware no pass************" + proxy['ip_port'])
            request.meta['proxy'] = "http://%s" % proxy['ip_port']