##学习笔记

### PyMySQL
* 安装: `pip install pymysql`


### 下载中间件 (Download Middleware)
* 编写下载中间件的四个主要方法
  * process_request(request, spider) - request对象经过下载中间件时会被调用，优先级高先调用
  * process_response(request, response, spider) - response对象经过下载中间件时会被调用, 优先级高后调用
  * process_exception(request, exception, spider) - 当process_request()和process_response()抛出异常时会被调用
  * from_crawler(cls, crawler) - 使用crawler来创建中间器对象，并(必须)返回一个中间件对象
* 如何enable自己编写的Download Middleware
  * 第一步: 在爬虫的"settings.py"文件里启用：
```python
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'maoyanmovie.middlewares.MaoyanmovieDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'maoyanmovie.middlewares.RandomHttpProxyMiddleware': 400,

}
HTTP_PROXY_LIST = [
    'http://104.248.63.15:30588',
    'http://45.77.71.140:9050',
]
```
  * 第二步: 编写自己的Middleware, 并且写入"middlewares.py"文件， 这样在爬虫启动的时候就会自己调用
  
 