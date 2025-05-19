# Python程序示例

## 项目概述
本项目包含三个Python程序，涵盖数据库操作与网络爬虫技术。所有代码均已测试通过，可直接运行。

---

## 程序1：学生信息管理系统
### 功能特性
- ✅ 控制台交互式操作
- ✅ 学生信息数据库存储
- ✅ 支持增删改查功能
- ✅ MySQL数据库连接

### 技术实现
```python
import pymysql
# 数据库配置
db = pymysql.connect(
    host="localhost",
    user="root",
    password="whbdgh8153",  # 需根据实际环境修改
    database="student"
)
```

### 运行指南
1. 创建MySQL数据库：
   ```sql
   CREATE DATABASE student;
   USE student;
   CREATE TABLE students (
       id VARCHAR(20) PRIMARY KEY,
       name VARCHAR(20),
       age INT,
       gender VARCHAR(10)
   );
   ```
2. 安装依赖：
   ```bash
   pip install pymysql
   ```
3. 运行程序：
   ```bash
   python 学生信息管理系统.py
   ```

---

## 程序2：图书信息爬虫
### 功能特性
- 🌐 爬取 [SPA5网站](https://spa5.scrape.center) 前5页数据
- 📚 提取字段：ID/书名/作者/封面图/评分
- 💾 自动保存为 `books.json`

### 核心代码片段
```python
def get_books():
    for page in range(1, 6):
        url = f"https://spa5.scrape.center/page/{page}"
        # 使用CSS选择器提取数据
        items = soup.select('.el-card')
```

### 运行方式
```bash
pip install requests beautifulsoup4
python 爬取图书网站.py
```

---

## 程序3：名人名言爬虫
### 功能特性
- 🕸️ 爬取 [Quotes网站](https://quotes.toscrape.com) 前10页数据
- ✍️ 提取字段：名言内容/作者/出生信息
- 📥 自动保存为 `quotes.json`

### 实现亮点
```python
def get_author_info(url):
    # 嵌套抓取作者详细信息
    date = soup.select_one('.author-born-date').text
    place = soup.select_one('.author-born-location').text
```

### 运行命令
```bash
pip install requests beautifulsoup4
python 爬取评论.py
```

---

## 注意事项
1. 数据库配置需根据本地环境修改
2. 爬虫程序需注意反爬策略，适当调整`time.sleep`
3. JSON文件将生成在程序同级目录
4. 确保运行前已安装所有依赖库

