# BeautifulSoup

`BeautifulSoup` 是一个用于解析 HTML 和 XML 文档的 Python 库。它提供了简单易用的 API，能够快速提取网页中的数据。以下是 `BeautifulSoup` 的主要功能和常用函数。

---

## 1.1 安装

使用以下命令安装 `BeautifulSoup`：

```bash
pip install beautifulsoup4
```

### 1.1.1 解析器

#### 解析器对比

| 解析器        | 速度 | 兼容性 | 依赖库     | 适用场景                                     |
| :------------ | :--- | :----- | :--------- | :------------------------------------------- |
| `html.parser` | 较慢 | 较好   | 无需安装   | 简单的 HTML 文档，无外部依赖场景             |
| `lxml`        | 快   | 好     | `lxml`     | 高性能解析，支持 HTML 和 XML                 |
| `html5lib`    | 慢   | 最好   | `html5lib` | 复杂的 HTML 文档（如浏览器兼容模式下的页面） |
| `xml`         | 快   | 好     | `lxml`     | 解析 XML 文档                                |

---

## 1.2 基本用法

```python
from bs4 import BeautifulSoup

# 示例 HTML
html = """
<html>
  <head><title>示例页面</title></head>
  <body>
    <p class="class_intro1">这是一个带有class标签的示例段落1。</p>
    <p class="class_intro2">这是一个带有class标签的示例段落2。</p>
    <p id="id_intro" class="class_intro1">这是一个带有id标签的示例段落。</p>
    <a class="class_intro" href="https://example1.com">这是一个示例链接1</a>
    <a id="id_intro" href="https://example2.com">这是一个示例链接2</a>
    <div>
      <ul>
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
        <li>赵六</li>
      </ul>
    </div>
  </body>
</html>
"""

# 创建 BeautifulSoup 对象（推荐使用 lxml 解析器，需提前安装：pip install lxml）
soup = BeautifulSoup(html, "lxml")

# 打印解析后的 HTML
print(soup.prettify())
```

---

## 1.3 常用函数

### 1.3.1 `find`

**功能**：查找第一个匹配的标签。

**语法**：
```python
find(name, attrs, recursive, string, **kwargs)
```

**参数**：
- `name`：标签名称（如 `"div"`）。
- `attrs`：标签属性（如 `{"class": "intro"}`）。
- `recursive`：是否递归查找（默认为 `True`）。
- `string`：标签内的文本内容。

**示例**：
```python
# 查找第一个 <p> 标签
p_tag = soup.find("p")
print(p_tag.text)  # 输出：这是一个带有class标签的示例段落1。

# 查找第一个 class 为 "class_intro" 的 <a> 标签
a_tag = soup.find("a", class_="class_intro")
print(a_tag["href"])  # 输出：https://example1.com
```

#### 练习答案
```python
# 查找第一个 <h1> 标签
h1_tag = soup.find("h1")

# 查找 id 为 "main" 的 div 元素
div_main = soup.find("div", id="main")

# 查找 class 为 "title" 的第一个元素
title = soup.find(class_="title")

# 查找同时具有 class="post" 和 data-category="python" 的第一个 article 元素
article = soup.find("article", {"class": "post", "data-category": "python"})
```

---

### 1.3.2 `find_all`

**功能**：查找所有匹配的标签。

**语法**：
```python
find_all(name, attrs, recursive, string, limit, **kwargs)
```

**参数**：
- `name`：标签名称（如 `"a"`）。
- `attrs`：标签属性（如 `{"href": True}`）。
- `recursive`：是否递归查找（默认为 `True`）。
- `string`：标签内的文本内容。
- `limit`：限制返回的结果数量。

**示例**：
```python
# 查找所有 <a> 标签
a_tags = soup.find_all("a")
for a in a_tags:
    print(a["href"])

# 查找所有 id 为 "id_intro" 的 <p> 标签
p_tags = soup.find_all("p", id="id_intro")
for p in p_tags:
    print(p.text)
```

#### 练习答案
```python
# 查找所有的 article 元素
articles = soup.find_all("article")

# 查找前 2 个 p 元素
p_tags = soup.find_all("p", limit=2)

# 查找所有具有 data-category 属性的元素
elements = soup.find_all(attrs={"data-category": True})
```

---

### 1.3.3 `select`

**功能**：使用 CSS 选择器查找标签。

**语法**：
```python
select(selector)
```

**参数**：
- `selector`：CSS 选择器（如 `"div.content > p"`）。

**示例**：
```python
# 查找所有 class 包含 "post" 的元素
posts = soup.select(".post")

# 查找 section 下的所有 article 元素
articles = soup.select("section article")

# 查找 class 为 "post" 且 "featured" 的元素
featured_post = soup.select(".post.featured")
```

#### 练习答案
```python
# 查找所有 h2 元素
h2_tags = soup.select("h2")

# 查找 data-category 值为 "python" 的所有元素
python_elements = soup.select("[data-category='python']")

# 查找 ul 的直接子元素 li
lis = soup.select("ul > li")
```

---

### 1.3.4 `get_text`

**功能**：获取标签内的文本内容。

**语法**：
```python
get_text(separator="", strip=False)
```

**示例**：
```python
p_tag = soup.find("p")
print(p_tag.get_text(strip=True))  # 去除前后空白
```

---

### 1.3.5 `attrs`

**功能**：获取标签的所有属性。

**语法**：
```python
tag.attrs
```

**示例**：
```python
a_tag = soup.find("a")
print(a_tag.attrs)  # 输出：{'class': ['class_intro'], 'href': 'https://example1.com'}
```

#### 综合练习答案
```python
# 获取所有文章链接
links = [a["href"] for a in soup.select("a.read-more")]

# 构建分类到文章标题的字典
categories = {}
for article in soup.find_all("article"):
    category = article.get("data-category")
    title = article.find("h2").get_text()
    categories.setdefault(category, []).append(title)
```

---

## 1.4 总结

- **`find`**：查找第一个匹配的标签。
- **`find_all`**：查找所有匹配的标签。
- **`select`**：使用 CSS 选择器查找标签。
- **`get_text`**：获取标签内的文本内容。
- **`attrs`**：获取标签的所有属性。

---

### 实战练习

#### 1. 提取表格数据为字典列表
```python
# HTML 表格示例
html_table = """
<table>
    <tr>
        <th>姓名</th>
        <th>年龄</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>25</td>
    </tr>
    <tr>
        <td>李四</td>
        <td>30</td>
    </tr>
</table>
"""

soup = BeautifulSoup(html_table, "lxml")
table_data = []
rows = soup.select("tr")
headers = [th.get_text() for th in rows[0].find_all("th")]
for row in rows[1:]:
    cells = row.find_all("td")
    row_dict = {headers[i]: cell.get_text() for i, cell in enumerate(cells)}
    table_data.append(row_dict)

print(table_data)  # 输出：[{'姓名': '张三', '年龄': '25'}, {'姓名': '李四', '年龄': '30'}]
```

#### 2. 爬取麦当劳汉堡信息
```python
import requests
from bs4 import BeautifulSoup

# 注意事项：
# 1. 检查网站 robots.txt 是否允许爬取
# 2. 添加请求头模拟浏览器访问
headers = {"User-Agent": "Mozilla/5.0"}

url = "https://www.mcdonalds.com.cn/index/Food/menu/burger"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# 提取汉堡名称和图片链接
burgers = []
for item in soup.select(".burger-item"):
    name = item.find("h3").get_text()
    img_url = item.find("img")["src"]
    burgers.append({"name": name, "image": img_url})

# 下载图片
for burger in burgers:
    response = requests.get(burger["image"])
    with open(f"{burger['name']}.jpg", "wb") as f:
        f.write(response.content)
```

---

**注意**：网络爬虫需遵守法律法规和目标网站的协议，避免对服务器造成过大压力。

---

### 附录：常见问题

#### 1. 如何处理多值 class？
```python
# 错误写法（无法匹配多值 class）
soup.find("div", class_="post featured")

# 正确写法（使用 CSS 选择器）
soup.select("div.post.featured")
```

#### 2. 如何提取嵌套标签的文本？
```python
# 直接提取会包含子标签的文本
div = soup.find("div")
print(div.get_text())  # 输出所有子标签的文本

# 仅提取当前标签的直接文本
print(div.find(text=True, recursive=False))
```

#### 3. 如何避免因标签不存在导致的错误？
```python
# 使用 try-except 或默认值
element = soup.find("div", id="non-existent")
if element:
    print(element.text)
else:
    print("未找到元素")
```

---

