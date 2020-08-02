# -*- coding: utf-8 -*-

# Scrapy settings for maoyanmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyanmovie'

SPIDER_MODULES = ['maoyanmovie.spiders']
NEWSPIDER_MODULE = 'maoyanmovie.spiders'

# Database settings
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 3306
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES = {
    'uuid_n_v': 'v1',
    'uuid': '30496260CBBB11EA9DCC5DD453C9604E6C868C06D42348119E66742AB1DC2FA9',
    'mojo-uuid': '6efed4c70fa61968d6ee272ef4b7e660',
    '_lxsdk_cuid': '30496260CBBB11EA9DCC5DD453C9604E6C868C06D42348119E66742AB1DC2FA9',
    '_lxsdk': '094DC040CB6411EA8A8375094482DFA4D0297F2A867F4419A03E2C61639BE876',
    '_lx_utm': 'utm_source%3Dgoogle%26utm_medium%3Dorganic',
    '_csrf': '8bbd4d85f71dda5188fa597f4a333adf651f212ef8e98aa77d3b48126a26765f',
    'mojo-session-id': '{"id":"51ab649bcd4a8513545872423e7d926d","time":1596294775217}',
    'lt': '1Qwbr3sY87yozF6xfNk6d00T1ysAAAAAHAsAAP7vycUldHdo1_I4Qkc1Y659iQ-AIK7iJL--3HFImrTKv32oIngC3889wSVa1Sbqzw',
    'lt.sig': 'Qh8W_gmnFrMRfz_b9vdmDxngg4s',
    'mojo-trace-id': '4',
    'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1595381463,1595904850',
    'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1595679013',
    '__mta': '108887101.1595381463864.1595987332442.1596294903548.13',
    '_lxsdk_s': '173aa9541db-b02-c36-525%7C%7C5',
}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyanmovie.middlewares.MaoyanmovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'maoyanmovie.middlewares.MaoyanmovieDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'maoyanmovie.middlewares.RandomHttpProxyMiddleware': 400,

}
HTTP_PROXY_LIST = [
    'http://101.4.136.34:81',
    'http://110.243.13.15:9999',
    'http://111.13.100.91:80',
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'maoyanmovie.pipelines.MaoyanmoviePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
