# requests

Python `requests` 库是用于发送 HTTP 请求的强大工具，其 API 设计简洁优雅，适合爬虫开发、API 调用等场景。

---

## 1.1 安装

使用 pip 安装最新版本：

```bash
pip install requests
```

---

## 1.2 基础用法

### 发送 GET 请求

```python
import requests

url = "https://www.baidu.com"
response = requests.get(url)

# 自动推断编码（解决中文乱码）
response.encoding = response.apparent_encoding

# 常用属性和方法
print(response.text)        # 响应文本（字符串）
print(response.content)     # 原始二进制数据（如图片）
print(response.status_code) # 状态码（200表示成功）
print(response.headers)     # 响应头（字典格式）
print(response.url)         # 实际请求的 URL（含重定向）
```

### GET vs POST 对比

| **方法** | **参数位置**   | **数据长度限制** | **典型场景**             |
| -------- | -------------- | ---------------- | ------------------------ |
| GET      | URL 查询参数   | 受 URL 长度限制  | 搜索、分页               |
| POST     | 请求体（Body） | 无理论限制       | 登录、表单提交、文件上传 |

---

## 1.3 发送带参数的请求

### GET 请求参数示例

```python
import requests

url = "https://www.baidu.com/s"
params = {"wd": "周杰伦"}  # 查询参数
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, params=params, headers=headers)
print(response.text)
```

#### 练习 1：基础 GET 请求
```python
# 向 https://httpbin.org/get 发送请求并打印响应
response = requests.get("https://httpbin.org/get")
print(f"状态码: {response.status_code}\n内容: {response.text}")
```

#### 练习 2：带查询参数的 GET 请求
```python
# 发送参数 name=Alice 和 age=25
params = {"name": "Alice", "age": 25}
response = requests.get("https://httpbin.org/get", params=params)
print(response.json()["args"])  # 提取服务器收到的参数
```

#### 练习 3：解析 JSON 数据
```python
# 获取 GitHub 用户信息
response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print(f"用户名: {data['login']}, 公司: {data.get('company', '未填写')}")
```

---

## 1.4 发送 POST 请求

### 表单提交示例

```python
import requests

url = "https://httpbin.org/post"
data = {"username": "test", "password": "123456"}  # 表单数据
headers = {"User-Agent": "MyApp/1.0"}

response = requests.post(url, data=data, headers=headers)
print(response.json()["form"])  # 提取表单数据
```

#### 练习 1：自定义请求头
```python
headers = {
    "User-Agent": "MyTestApp/1.0",
    "X-Custom-Header": "HelloWorld"
}
response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json()["headers"])
```

#### 练习 2：超时与异常处理
```python
try:
    response = requests.get("https://httpbin.org/delay/5", timeout=3)
except requests.exceptions.Timeout:
    print("请求超时！")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
```

---

## 1.5 会话管理（Session）

```python
import requests
from bs4 import BeautifulSoup

# 创建 Session 对象保持会话
session = requests.Session()
login_url = "https://www.gushiwen.cn/user/login.aspx"

# 1. 获取动态参数（VIEWSTATE 和验证码）
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
viewstate = soup.select_one("#__VIEWSTATE")["value"]
viewstategen = soup.select_one("#__VIEWSTATEGENERATOR")["value"]

# 2. 下载验证码
code_url = "https://www.gushiwen.cn" + soup.select_one("#imgCode")["src"]
code_response = session.get(code_url)
with open("code.jpg", "wb") as f:
    f.write(code_response.content)

# 3. 提交登录表单
code = input("请输入验证码: ")
data = {
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategen,
    "email": "your@email.com",
    "pwd": "your_password",
    "code": code,
    "denglu": "登录"
}
login_response = session.post(login_url, data=data)
print("登录成功！" if "退出登录" in login_response.text else "登录失败")
```

---

## 1.6 综合案例：爬取电影数据

```python
import requests
from bs4 import BeautifulSoup
import json

url = "https://ssr1.scrape.center/page/1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []
for item in soup.select(".el-card"):
    name = item.select_one("h2").text.strip()
    score = item.select_one(".score").text.strip()
    categories = [c.text.strip() for c in item.select(".categories button")]
    published = item.select_one(".info:contains('上映')").text.split("：")[-1].strip()
    drama = item.select_one(".drama p").text.strip()

    movies.append({
        "电影名称": name,
        "电影分数": score,
        "电影类别": categories,
        "上映时间": published,
        "简介": drama
    })

# 保存为 JSON 文件
with open("movies.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=2)
```

---

## 1.7 注意事项

1. **编码处理**：
   ```python
   response.encoding = response.apparent_encoding  # 自动推断编码
   ```

2. **反爬策略**：
   - 设置合理的 `User-Agent` 和 `Referer`
   - 使用代理 IP（示例）：
     ```python
     proxies = {"http": "http://10.10.1.10:3128"}
     response = requests.get(url, proxies=proxies)
     ```

3. **JSON 解析**：
   ```python
   data = response.json()  # 直接转换为字典
   ```

4. **文件下载**：
   ```python
   with open("image.jpg", "wb") as f:
       f.write(response.content)
   ```

---

