##学习笔记


### 异常的捕获和处理
* 学习到了 pretty_errors这个库
* 运用到了异常处理在数据库的连接和读写之中

### PyMySQL
* 安装: `pip install pymysql`
* 学习了如何在pymysql里面创建数据库，创建表格以及插入数据
* 期待ORM部分的学习

### 反爬虫和反反爬虫
* 无论是那个工具，原理都是模拟浏览器
* 反爬虫是根据请求和行为来判断是否爬虫
* 浏览器的基本行为
  * 带HTTP的头信息，比如 user-agent, referer等
  * 带cookies (包含加密的用户名，密码验证信息)
* 通过F12抓包，获取真正的请求头部信息
* 使用fake_useragent的第三方库


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
  
### WebDriver
* 针对页面被Java Script加密的情况，或者是页面获取不到我们想要去请求的URL的情况。
* 让Python去模拟浏览器点击的行为 (比如填写用户名和密码)
