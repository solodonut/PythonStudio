# -*- coding: utf-8 -*-

# Scrapy settings for jd_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

"""
常用参数说明：
1. DNS_TIMEOUT默认60s

2. DOWNLOADER_MIDDLEWARES下载中间件

3. DOWNLOAD_DELAY两次下载的间隔

4. DOWNLOAD_TIMEOUT默认180s

5. DOWNLOAD_MAXSIZE默认1024M

6. LOG_ENABLED

7. LOG_FILE默认是NONE

8. LOG_LEVEL，默认是DEBUG，即打印DEBUG, INFO, WARNING, ERROR，所有LOG信息

9. LOG_STDOUT，默认是false，所有的标准输出是否放在log中

10. MEMDEBUG_ENABLED，默认是false

11. RANDOMIZE_DOWNLOAD_DELAY默认是true, 等待0.5-1.5*DOWNLOAD_DELAY时间，防止被禁

12. USER_AGENT默认是”Scrapy/VERSION （+http://scrapy.org）

"""


BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]

# 这里使用的代理IP，因为IP的存活期的限制，请定期更新下面的IP，可从http://www.xicidaili.com/ 中找免费的代理IP
PROXIES = [
    {'ip_port': '116.252.135.244:8998', 'user_pass': ''},
    {'ip_port': '115.197.136.194:8118', 'user_pass': ''},
    {'ip_port': '114.231.71.48:8088', 'user_pass': ''},
    {'ip_port': '120.92.3.127:80', 'user_pass': ''},
    {'ip_port': '124.88.67.63:80', 'user_pass': ''},
    {'ip_port': '124.88.67.52:843', 'user_pass': ''},
    {'ip_port': '122.72.32.73:80', 'user_pass': ''},
    {'ip_port': '1.63.239.136:8118', 'user_pass': ''},
    {'ip_port': '116.31.26.15:8118', 'user_pass': ''},
    {'ip_port': '222.61.20.147:808', 'user_pass': ''},
    {'ip_port': '117.69.22.50:8118', 'user_pass': ''},
    {'ip_port': '115.50.55.197:8118', 'user_pass': ''},
    {'ip_port': '119.254.84.90:80', 'user_pass': ''},
    {'ip_port': '119.162.52.140:8118', 'user_pass': ''},
    {'ip_port': '121.204.165.93:8118', 'user_pass': ''},
    {'ip_port': '27.159.126.82:8118', 'user_pass': ''},
    {'ip_port': '119.254.92.52:80', 'user_pass': ''},
    {'ip_port': '124.88.67.10:80', 'user_pass': ''},
    {'ip_port': '121.61.104.145:8118', 'user_pass': ''},
    {'ip_port': '121.204.165.77:8118', 'user_pass': ''},
    {'ip_port': '203.91.121.74:3128', 'user_pass': ''},
    {'ip_port': '119.29.103.13:8888', 'user_pass': ''},
    {'ip_port': '220.160.22.115:80', 'user_pass': ''},
    {'ip_port': '124.88.67.83:80', 'user_pass': ''},
    {'ip_port': '210.45.240.249:3128', 'user_pass': ''},
    {'ip_port': '203.70.11.186:80', 'user_pass': ''},
    {'ip_port': '124.88.67.81:80', 'user_pass': ''},
    {'ip_port': '218.76.106.78:3128', 'user_pass': ''},
    {'ip_port': '182.254.158.70:8088', 'user_pass': ''},
    {'ip_port': '58.246.194.70:8080', 'user_pass': ''},
    {'ip_port': '202.98.152.138:80', 'user_pass': ''},
    {'ip_port': '218.66.253.146:8800', 'user_pass': ''},
    {'ip_port': '59.61.89.229:8800', 'user_pass': ''},
    {'ip_port': '59.61.89.233:8800', 'user_pass': ''},
    {'ip_port': '58.213.19.233:10081', 'user_pass': ''},
    {'ip_port': '175.180.248.11:8080', 'user_pass': ''},
    {'ip_port': '218.103.60.205:8080', 'user_pass': ''},
    {'ip_port': '222.89.10.28:9000', 'user_pass': ''},
    {'ip_port': '183.39.159.236:9797', 'user_pass': ''},
    {'ip_port': '119.131.66.98:9797', 'user_pass': ''},
    {'ip_port': '113.111.149.193:9797', 'user_pass': ''},
    {'ip_port': '202.118.8.13:3128', 'user_pass': ''},
    {'ip_port': '58.67.159.50:80', 'user_pass': ''},
    {'ip_port': '59.61.89.230:8800', 'user_pass': ''},
    {'ip_port': '106.14.38.97:46985', 'user_pass': ''},
    {'ip_port': '27.159.127.129:8118', 'user_pass': ''},
    {'ip_port': '123.138.216.94:9999', 'user_pass': ''},
    {'ip_port': '101.251.199.66:3128', 'user_pass': ''},
    {'ip_port': '162.105.80.111:3128', 'user_pass': ''},
    {'ip_port': '182.121.206.80:9999', 'user_pass': ''},
    {'ip_port': '111.202.154.88:8080', 'user_pass': ''},
    {'ip_port': '221.204.100.92:9797', 'user_pass': ''},
    {'ip_port': '220.135.150.211:3128', 'user_pass': ''},
    {'ip_port': '118.171.58.151:8080', 'user_pass': ''},
    {'ip_port': '61.228.51.246:8080', 'user_pass': ''},
    {'ip_port': '218.56.132.157:8080', 'user_pass': ''},
    {'ip_port': '121.69.47.218:9797', 'user_pass': ''},
    {'ip_port': '123.13.204.222:9797', 'user_pass': ''},
    {'ip_port': '101.254.232.74:9999', 'user_pass': ''},
    {'ip_port': '110.72.49.15:9999', 'user_pass': ''},
    {'ip_port': '113.200.159.155:9999', 'user_pass': ''},
    {'ip_port': '106.115.190.105:9797', 'user_pass': ''},
    {'ip_port': '59.44.244.14:9797', 'user_pass': ''},
    {'ip_port': '61.152.81.193:9100', 'user_pass': ''},
    {'ip_port': '124.128.221.27:8080', 'user_pass': ''},
    {'ip_port': '125.40.27.233:9797', 'user_pass': ''},
    {'ip_port': '49.115.62.10:8088', 'user_pass': ''},
    {'ip_port': '183.185.2.30:9797', 'user_pass': ''},
    {'ip_port': '118.178.182.47:23687', 'user_pass': ''},
    {'ip_port': '119.123.237.252:9797', 'user_pass': ''},
    {'ip_port': '58.251.152.233:80', 'user_pass': ''},
    {'ip_port': '116.17.127.136:9999', 'user_pass': ''},
    {'ip_port': '61.141.94.83:9000', 'user_pass': ''},
    {'ip_port': '36.234.177.10:8888', 'user_pass': ''},
    {'ip_port': '114.42.227.89:3128', 'user_pass': ''},
    {'ip_port': '114.42.63.193:3128', 'user_pass': ''},
    {'ip_port': '124.88.67.30:80', 'user_pass': ''},
    {'ip_port': '59.40.86.158:9797', 'user_pass': ''},
    {'ip_port': '113.108.141.98:9797', 'user_pass': ''},
    {'ip_port': '27.46.43.40:9797', 'user_pass': ''},
    {'ip_port': '113.111.210.185:808', 'user_pass': ''},
    {'ip_port': '113.111.211.182:808', 'user_pass': ''},
    {'ip_port': '125.93.148.163:9000', 'user_pass': ''},
    {'ip_port': '125.93.149.178:9000', 'user_pass': ''},
    {'ip_port': '110.84.35.200:3128', 'user_pass': ''},
    {'ip_port': '58.52.201.118:8080', 'user_pass': ''},
    {'ip_port': '219.216.96.87:3128', 'user_pass': ''},
    {'ip_port': '119.129.96.113:9797', 'user_pass': ''},
    {'ip_port': '113.18.193.23:80', 'user_pass': ''},
    {'ip_port': '211.153.17.151:80', 'user_pass': ''},
    {'ip_port': '218.58.52.106:9999', 'user_pass': ''},
    {'ip_port': '124.206.107.125:3128', 'user_pass': ''},
    {'ip_port': '180.97.237.199:8080', 'user_pass': ''},
    {'ip_port': '119.127.200.5:9999', 'user_pass': ''},
    {'ip_port': '118.171.187.48:3128', 'user_pass': ''},
    {'ip_port': '113.99.111.53:9797', 'user_pass': ''},
    {'ip_port': '60.167.22.188:8118', 'user_pass': ''},
    {'ip_port': '118.171.60.37:8080', 'user_pass': ''},
    {'ip_port': '219.145.123.249:9797', 'user_pass': ''},
    {'ip_port': '219.132.43.107:9797', 'user_pass': ''},
    {'ip_port': '221.205.89.100:9797', 'user_pass': ''},
    {'ip_port': '218.6.145.11:9797', 'user_pass': ''},
    {'ip_port': '218.68.225.21:9797', 'user_pass': ''},
    {'ip_port': '115.183.11.158:9999', 'user_pass': ''},
    {'ip_port': '14.115.50.195:9999', 'user_pass': ''},
    {'ip_port': '123.138.73.122:9999', 'user_pass': ''},
    {'ip_port': '59.47.7.82:8080', 'user_pass': ''},
    {'ip_port': '211.103.250.145:80', 'user_pass': ''},
    {'ip_port': '211.103.250.146:80', 'user_pass': ''},
    {'ip_port': '58.249.55.222:9797', 'user_pass': ''},
    {'ip_port': '113.65.10.136:9797', 'user_pass': ''},
    {'ip_port': '119.53.185.204:9000', 'user_pass': ''},
    {'ip_port': '58.60.32.86:9797', 'user_pass': ''},
    {'ip_port': '221.232.80.134:8080', 'user_pass': ''},
    {'ip_port': '27.46.50.248:9797', 'user_pass': ''},
    {'ip_port': '183.61.163.59:8080', 'user_pass': ''},
    {'ip_port': '116.28.160.126:9999', 'user_pass': ''},
    {'ip_port': '116.17.139.55:9797', 'user_pass': ''},
    {'ip_port': '123.139.56.234:9999', 'user_pass': ''},
    {'ip_port': '27.46.37.188:9797', 'user_pass': ''},

]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = 2  # 为防止封杀IP，每次爬一次有一定延迟，要速度可以注释
RANDOMIZE_DOWNLOAD_DELAY = True  # 随机等待时间，防止被封IP


# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    'jd_spider.middlewares.RandomUserAgent': 1,
    'jd_spider.middlewares.ProxyMiddleware': 100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jd_spider.pipelines.MySQLPipeline': 300,  # 抓取商品信息时，使用该通道
    # 'jd_spider.pipelines.CommentPipeline': 300,  # 抓取评论信息时，使用该通道
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Retry many times since proxies often fail
RETRY_TIMES = 10

# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
DOWNLOAD_TIMEOUT = 600  # 下载超时时间

# LOG_LEVEL = 'INFO'
# LOG_LEVEL = 'WARNING'
LOG_FILE = 'jd_spider.log'

# 数据库的配置，请将下面的换成你自己的数据库配置
POOL_NAME = 'jd_pool'  # 连接池名称
POOL_SIZE = 3  # 连接池连接数
DB_HOST = 'localhost'  # 主机名
DB_PORT = 3306  # 端口号
DB_USER = 'root'    # 用户名
DB_PASSWD = 'wqoeap3t'  # 密码
DB_DB = 'JD'  # 数据库名


