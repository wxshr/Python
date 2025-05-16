---

### **1. 安装与解析器选择**
```python
soup = BeautifulSoup(html, "lxml")
```
- **为什么用 `lxml` 解析器？**  
  - `lxml` 解析速度快、兼容性好，支持 HTML 和 XML，适合大多数场景。
  - 若未安装 `lxml`，需先运行 `pip install lxml`。
  - **思考延伸**：如果处理的是不规范 HTML（如网页残缺），可用 `html5lib`。

---

### **2. 基本用法：解析 HTML**
```python
print(soup.prettify())
```
- **功能**：格式化输出 HTML，便于查看结构。
- **实现逻辑**：BeautifulSoup 将原始 HTML 转换为树形结构，`prettify()` 添加缩进和换行。
- **思考延伸**：调试时常用此方法确认解析结果是否符合预期。

---

### **3. `find` 方法**
#### 示例 1：查找第一个 `<p>` 标签
```python
p_tag = soup.find("p")
```
- **逻辑**：通过标签名 `"p"` 定位第一个段落标签。
- **关键点**：`find()` 返回第一个匹配的标签对象，未找到返回 `None`。

#### 示例 2：查找特定属性的 `<a>` 标签
```python
a_tag = soup.find("a", class_="class_intro")
```
- **参数解析**：
  - `class_`：因 `class` 是 Python 关键字，需加下划线。
  - 等效写法：`soup.find("a", {"class": "class_intro"})`。
- **思考延伸**：若属性值为多个（如 `class="post featured"`），需用字典或 CSS 选择器。

---

### **4. `find_all` 方法**
#### 示例 1：查找所有 `<a>` 标签
```python
a_tags = soup.find_all("a")
```
- **逻辑**：返回所有 `<a>` 标签的列表。
- **应用场景**：批量提取链接或文本。

#### 示例 2：限制结果数量
```python
p_tags = soup.find_all("p", limit=2)
```
- **参数 `limit`**：限制返回前 2 个结果，提升性能。
- **思考延伸**：若需分页处理数据，可结合循环和 `limit`。

---

### **5. `select` 方法（CSS 选择器）**
#### 示例 1：查找所有类为 `post` 的元素
```python
posts = soup.select(".post")
```
- **逻辑**：`.` 表示类选择器，等价于 `class="post"`。
- **优势**：语法简洁，支持复杂嵌套（如 `div > ul > li`）。

#### 示例 2：多条件选择
```python
featured_post = soup.select(".post.featured")
```
- **逻辑**：`.post.featured` 表示同时具有 `post` 和 `featured` 类。
- **思考延伸**：CSS 选择器可组合属性选择器（如 `[data-category="python"]`）。

---

### **6. 提取文本与属性**
#### 示例 1：`get_text()`
```python
p_text = p_tag.get_text(strip=True)
```
- **参数 `strip`**：去除文本前后空格，避免脏数据。
- **注意**：若标签包含子标签，`get_text()` 会提取所有嵌套文本。

#### 示例 2：`attrs`
```python
a_attrs = a_tag.attrs
print(a_attrs["href"])  # 输出链接
```
- **逻辑**：`attrs` 返回标签属性的字典，可通过键直接访问。
- **容错处理**：建议用 `a_tag.get("href")`，避免键不存在时报错。

---

### **7. 实战练习解析**
#### 练习 1：提取表格数据
```python
rows = soup.select("tr")
headers = [th.get_text() for th in rows[0].find_all("th")]
```
- **逻辑**：
  1. 通过 `tr` 选择所有行。
  2. 第一行的 `<th>` 作为表头。
  3. 遍历后续行，将 `<td>` 内容与表头映射为字典。
- **思考延伸**：处理动态表格时，需检查是否存在 `<thead>` 和 `<tbody>`。

#### 练习 2：爬取麦当劳汉堡信息
```python
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
```
- **关键点**：
  - 添加 `User-Agent` 请求头，模拟浏览器访问。
  - 检查 `robots.txt` 是否允许爬取。
- **容错处理**：需用 `try-except` 捕获网络请求异常。

---

### **总结：思考路径**
1. **明确目标**：确定要提取的数据类型（如文本、链接、属性）。
2. **分析 HTML 结构**：使用开发者工具查看标签层级和属性。
3. **选择定位方式**：
   - 简单场景：`find()`/`find_all()`。
   - 复杂嵌套：CSS 选择器 `select()`。
4. **处理数据**：
   - 提取文本：`get_text()`。
   - 提取属性：`tag["attr"]` 或 `tag.get("attr")`。
5. **异常处理**：检查标签是否存在，避免 `None` 引发的错误。

---

### **常见陷阱与优化**
- **重复的 `id`**：HTML 中 `id` 应唯一，若页面不规范可能导致提取错误。
- **动态内容**：BeautifulSoup 无法解析 JavaScript 动态生成的内容，需结合 Selenium。
- **性能优化**：避免频繁解析整个文档，尽量使用精确选择器减少搜索范围。
