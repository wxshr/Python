
# Python urllib 模块学习笔记

---

## 一、网页爬取流程概览

### 1. 明确爬取目标

- **确定需求**：明确要爬取的数据类型（如文本、图片、视频、商品信息等）。
- **选择目标网站**：分析网站结构（URL规律、页面渲染方式等）。
- **检查合法性**：查看网站的 `robots.txt` 文件，确认是否允许爬取。

### 2. 发送 HTTP 请求

- **工具选择**：
  - 常用库：`urllib`（标准库）、`requests`（更简洁）、`aiohttp`（异步）。
  - 模拟浏览器：`selenium`、`playwright`（处理动态页面）。

- **请求类型**：
  - `GET`：用于获取数据。
  - `POST`：用于提交表单等。

- **设置请求头（如 User-Agent）**：模拟浏览器，防止被反爬。

### 3. 解析网页内容

- **静态页面（HTML）**：
  - 工具：`BeautifulSoup`、`lxml`、正则表达式等。
  
- **动态页面（AJAX/JS 渲染）**：
  - 使用 `selenium`/`playwright` 模拟浏览器。
  - 或通过浏览器开发者工具抓接口。

### 4. 数据提取与清洗

- **字段提取**：如标题、价格、评论等。
- **清洗技巧**：
  - 去除空白字符：`strip()`。
  - 编码处理：如 `decode('utf-8')`。
  - 过滤空值、广告等无效信息。

### 5. 数据存储

- **文件存储**：CSV（`pandas`）、JSON、文本等。
- **数据库**：MySQL（`pymysql`）、MongoDB（`pymongo`）等。

### 6. 反爬机制应对

- 随机 UA、IP代理、验证码识别、限速爬取（`time.sleep()`）。
- 合理设置请求频率，避免封 IP。

---

## 二、urllib 模块详解

`urllib` 是 Python 标准库中处理 URL 的模块，支持请求发送、编码解析、异常处理等功能。

### 2.1 模块结构

| 子模块 | 功能 |
|--------|------|
| `urllib.request` | 发送请求 |
| `urllib.parse` | URL 解析与构建 |
| `urllib.error` | 请求异常处理 |
| `urllib.robotparser` | 解析 `robots.txt` |

---

## 三、urllib.request 使用详解

### 3.1 发送 GET 请求

```python
from urllib.request import urlopen

url = "http://www.baidu.com"
response = urlopen(url)

# 读取响应内容
content = response.read().decode('utf-8')
print(content)
```

### 3.2 响应对象常用方法

```python
from urllib.request import urlopen
import http.client

response: http.client.HTTPResponse = urlopen("http://www.baidu.com")

print(response.getcode())      # 状态码
print(response.geturl())       # URL
print(response.getheaders())   # 响应头
```

---

### 3.3 下载文件

```python
import urllib.request

# 下载网页
urllib.request.urlretrieve("http://www.baidu.com", "baidu.html")

# 下载图片
img_url = "https://www.python.org/static/img/python-logo.png"
urllib.request.urlretrieve(img_url, "python-logo.png")
```

#### 下载进度显示

```python
from urllib.request import urlretrieve

def report_hook(blocknum, blocksize, totalsize):
    percent = min(blocknum * blocksize / totalsize, 1.0) * 100
    print(f"下载进度: {percent:.2f}%")

urlretrieve("https://www.baidu.com/robots.txt", "robots.txt", reporthook=report_hook)
```

---

## 四、urllib.parse 解析与构建 URL

```python
from urllib.parse import urlparse

url = "https://www.example.com:8080/path/page?query=python#frag"
parsed = urlparse(url)

print(parsed.scheme)
print(parsed.hostname)
print(parsed.port)
print(parsed.path)
print(parsed.query)
print(parsed.fragment)
```

### URL 编码与构建

```python
from urllib.parse import quote, urlencode

text = "Python 编程 & urllib"
print(quote(text))  # 编码

params = {'wd': '周杰伦', 'sex': '男'}
print(urlencode(params))
```

---

## 五、设置 User-Agent 模拟浏览器

```python
from urllib.request import Request, urlopen

url = "http://httpbin.org/user-agent"
headers = {'User-Agent': 'Mozilla/5.0 ...'}

req = Request(url, headers=headers)
res = urlopen(req)
print(res.read().decode('utf-8'))
```

---

## 六、发送 POST 请求

```python
import urllib.request
import urllib.parse
import json

url = "https://fanyi.baidu.com/sug"
data = {'kw': 'love'}
data = urllib.parse.urlencode(data).encode('utf-8')

headers = {'User-Agent': 'Mozilla/5.0 ...'}

req = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(req)

result = response.read().decode('utf-8')
print(json.loads(result))
```

---

## 七、代理设置

```python
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

proxies = {
    "http": "http://user:pwd@proxy:port",
    "https": "http://user:pwd@proxy:port"
}

proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)

url = "http://httpbin.org/ip"
res = opener.open(url)
print(res.read().decode())
```

---

## 八、Cookie 登录

```python
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 ...',
    'Cookie': 'your_cookie_here'
}

req = urllib.request.Request("https://www.example.com/personal", headers=headers)
response = urllib.request.urlopen(req)

with open("personal.html", "wb") as f:
    f.write(response.read())
```

---

## 九、综合示例：爬取豆瓣电影 Top250

```python
import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0 ...'}

for page in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={page}&filter="
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')

    filename = f"top250_page_{page//25+1}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
```

---

## 🔔 注意事项

1. **遵守法律法规**，不要爬取隐私、敏感信息。
2. **尊重网站服务**，合理控制访问频率，避免影响服务器。
3. **加强异常处理**，防止程序崩溃。
