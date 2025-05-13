## 1. python

### 1.1 下载python环境

https://www.python.org/downloads

### 1.2 第一个python程序 

```python
print('hello,world')
```

## 2. 基础语法

### 2.1 字面量

在代码中，被写下来的**固定值**，表示具体的、明确的数据值，称之为字面量，不需要通过计算或变量引用，而是直接表示其自身的值

### 2.2 注释

**在程序代码中对程序代码进行解释说明的文字**

```python
# 这是一段单行注释

"""
	这是多行注释（多用于对类，方法进行解释）
"""
```

### 2.3 变量

**在程序运行时**，能储存计算结果或能表示值的抽象概念

变量名称 = 存储的值

- **变量是数据的引用**：Python 中的变量本质上是对象的引用（类似指针），而不是直接存储数据。例如：

  ```python
  a = 10  # a 指向整数 10
  b = "hello"  # b 指向字符串 "hello"
  ```

- **动态类型**：变量无需声明类型，类型由赋值的对象决定，且可以随时改变：

  ```python
  x = 5      # x 是整数
  x = "hi"   # 现在 x 是字符串
  ```

#### 2.3.1 变量的赋值

- 直接赋值：

  ```python
  name = "Alice"
  ```

- 多变量同时赋值：

  ```python
  x, y, z = 1, 2, 3  # 分别赋值
  a = b = c = 0      # 多个变量指向同一值
  ```

- 交换变量值：

  ```python
  """
  	1.定义a=10,b=20
  	交换a,b的值，使a=20,b=10
  """
  ```

| **字面量**                                | **变量**                           |
| :---------------------------------------- | :--------------------------------- |
| 直接表示固定的值（如 `42`, `"hello"`）    | 存储值的名称（如 `x = 42`）        |
| 不可变（如 `3.14` 始终是 `3.14`）         | 可变（`x = 10` 可以变成 `x = 20`） |
| 不占用额外内存（Python 会缓存部分字面量） | 占用内存存储值                     |

### 2.4 数据类型

| 类型   | 描述       | 说明                  |
| ------ | ---------- | --------------------- |
| string | 字符串类型 | 用引号引起来的数据    |
| int    | 整型       | 存放整形：1，10，-1   |
| float  | 浮点型     | 存放小数：-3.14，5.55 |
| bool   | 布尔类型   | True,Flase            |

#### 2.4.1 type()

通过type()语句来得到数据的类型

```python
a = 10
print(type(a))
```

**练习**

```python
"""
定义一个变量 data，依次赋值为 100、"hello"、3.55，每次赋值后打印其类型。
预期输出：
<class 'int'>
<class 'str'>
<class 'float'>
"""
```

### 2.5 字符串定义方式

```python
str1 = "双引号"
str2 = '单引号'
str3 = """三引号"""
```

### 2.6 类型转换

| 函数    | 说明             |
| ------- | ---------------- |
| int()   | 转换为一个整数   |
| float() | 转换为一个浮点数 |
| str()   | 转换为字符串     |

**练习**

```python
"""
	1. 定义一个字符串s = ‘3.14’
	将它转换成整形
"""
```

### 2.7 标识符

在Python程序中，我们可以给很多东西起名字，比如：

- 变量的名字
- 方法的名字
- 类的名字,等等

这些名字，我们把它统一的称之为标识符，用来做内容的标识。

#### 2.7.1 命名规则

- **内容限定：** 只允许出现英文，中文，数字(不可以开头)，下划线（_）

- **大小写敏感**

- **不可使用关键字**

  

  ![](./images/关键字.png)

#### 2.7.2 命名规范

- **变量名:** 见名知意，下划线命名法，英文字母全小写

  ```python
  a = "zhangsan"
  b = 20
  
  name = "zhangsan"
  age = 20
  ```

- 类名

- 方法名

  

### 2.8 运算符

#### 2.8.1 算术运算符

| 运算符 | 描述 |
| ------ | ---- |
| **+**  | 加   |
| **-**  | 减   |
| *****  | 乘   |
| **/**  | 除   |
| //     | 整除 |
| %      | 取余 |
| **     | 指数 |

#### 2.8.1 赋值运算符

| 运算符 | 描述             |
| ------ | ---------------- |
| =      | 赋值运算符       |
| +=     | 加法赋值运算符   |
| -=     | 减法赋值运算符   |
| *=     | 乘法赋值运算符   |
| /=     | 除法赋值运算符   |
| %=     | 取模赋值运算符   |
| **=    | 幂赋值运算符     |
| //=    | 取整除赋值运算符 |



## 3. 字符串

### 3.1 定义格式

- **单引号**

- **双引号**

- **三引号**

  

### 3.2 字符串拼接

```python
print("hello,"+"world")
```

**注意事项:无法和非字符串类型进行拼接**

### 3.3 格式化

```python
var1 = "world"
var2 = "hello, %s" % var1

print(var2)
# %s表示占位符

name = "zhangsan"
age = 20
message = "我的姓名是%s,年龄为%s" %(name,age)
print(message)
```

| 格式符号 | 转化                             |
| -------- | -------------------------------- |
| %s       | 将内容转换成字符串，放入占位位置 |
| %d       | 将内容转换成整数，放入占位位置   |
| %f       | 将内容转换成浮点型，放入占位位置 |

#### 3.3.1 精度控制

```python
price = 3.6

info = "一个苹果的价格为%f" % price

print(info)
#一个苹果的价格为3.600000
```

我们可以使用辅助符号"m.n"来控制数据的宽度和精度

- m，控制宽度，要求是数字（很少使用）,设置的宽度小于数字自身，不生效
- .n，控制小数点精度，要求是数字，会进行小数的四舍五入

#### 3.3.2 快速写法

```python
price = 3.6
print(f"一个苹果的价格为:{price})
```

### 3.4 数据输入函数

```python
name = input("请输入的你的姓名:")
print(name)
```

**练习**

```python
"""
	定义两个变量，用以获取从键盘输入的内容，并给出提示信息:
	1.user_name,记录用户姓名
	2.user_age,记录用户年龄
	
	通过格式化字符串的形式，通过print语句输出:
	你好，我叫张三，今年20岁啦！
"""
```

## 4. 分支语句

#### 布尔类型

**bool:** True表示真，Flase表示假

```python
print(5>1)
```

####  比较运算符

| 运算符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| ==     | 判断内容是否相等，满足为True，不满足为False                  |
| !=     | 判断内容是否不相等，满足为True，不满足为False                |
| >      | 判断运算符左侧内容是否大于右侧，满足为True，不满足为False    |
| <      | 判断运算符左侧内容是否小于右侧，满足为True，不满足为False    |
| >=     | 判断运算符左侧内容是否大于等于右侧，满足为True，不满足为False |
| <=     | 判断运算符左侧内容是否小于等于右侧，满足为True，不满足为False |
| and    | 逻辑与（都真）                                               |
| or     | 逻辑或（任一真）                                             |
| not    | 逻辑非（取反）                                               |

### 4.1 if 

**最基本的条件判断结构，当条件为真时执行代码块。**

```python
if 判断条件：
	条件成立时，执行语句
```

**注意事项**

- 判断条件的结果一定要是布尔类型

- 不要忘记判断条件后的： 引号

- 归属于if语句的代码块，需在前方填充4个空格缩进

- 如果条件为 False，则跳过整个 if 块

  

**练习**

```python
"""
	1.通过input语句，获取键盘输入，为变量身高height赋值
	2.通过判断是否高于160，满足条件则输出以下信息:
	
	您的身高高于160，需要买票。

"""
```

### 4.2 if else

**当需要处理条件不成立的情况时使用。**

```python
if 判断条件：
	条件成立时，执行语句
else:
  不满足条件时，执行语句
```

**特点：**

- 确保总会执行其中一个代码块
- else 语句不需要条件
- else 必须与 if 配对使用

**示例：**

```python
age = 16
if age >= 18:
    print("欢迎进入")
else:
    print("未成年人禁止入内")
```

**练习**

```python
"""
	1.通过input语句，获取键盘输入，为变量身高height赋值
	2.通过判断是否高于160，满足条件则输出以下信息:
	您的身高高于160，需要买票。
  不满足条件则输出以下信息:
  您不需要买票，可以免费游玩。
"""
```

### 4.3 if elif else

**处理多个互斥条件时使用。**

```python
if 判断条件1：
	条件成立时，执行语句1
elif: 判断条件2:
  条件成立时，执行语句2
elif: 判断条件3:
  条件成立时，执行语句3 
else:
  都不满足条件时，执行语句4
```

**重要特性：**

- elif 是"else if"的缩写，可以有多个
- 条件判断是顺序进行的，一旦某个条件满足，后续条件不再检查
- else 是可选的，可以省略
- 整个结构只会执行一个代码块

### 4.4 嵌套使用

**概念：**
在一个分支结构的代码块中嵌套另一个完整的分支结构

```python
age = 25
membership = True

if age >= 18:
    if membership:
        print("尊贵的会员，欢迎光临VIP区域")
    else:
        print("欢迎进入普通区域")
else:
    print("未成年人禁止入内")
```

**练习**

```python
"""
	三角形类型判断：
		输入三个边长，判断是否能构成三角形及三角形类型：
			任意两边之和大于第三边才能构成三角形
				等边三角形：三边相等
				等腰三角形：两边相等
				直角三角形：a² + b² = c²（需考虑各种排列组合）
				普通三角形：其他情况
"""
```

### 4.5 单行条件表达式（三元运算符）

**简化简单的 if-else 结构。**

```python
值1 if 条件 else 值2
```

**特点：**

- 简洁的条件赋值方式
- 返回两个值中的一个
- 不适合复杂的逻辑

**示例：**

```python
# 传统写法
if x > y:
    max_val = x
else:
    max_val = y

# 三元运算符写法
max_val = x if x > y else y
```

### 4.6 布尔运算符在条件中的使用

Python 支持在条件中使用 and、or、not 组合多个条件

**示例：**

```python
age = 25
income = 45000
is_weekend = True

# and 运算符
if age >= 18 and income > 40000:
    print("符合贷款条件")

# or 运算符
if age < 12 or age > 65:
    print("可享受票价优惠")

# not 运算符
if not is_weekend:
    print("工作日票价")
```

**短路特性：**

- 对于 `and`，如果第一个条件为 False，不会计算第二个条件
- 对于 `or`，如果第一个条件为 True，不会计算第二个条件

### 4.7 Python 3.10+ 的 match-case 语句

**基础语法：**

```python
match 变量:
    case 模式1:
        # 匹配模式1时执行
    case 模式2:
        # 匹配模式2时执行
    case _:
        # 默认情况
```

**常见用法：**

**简单值匹配：**

```python
status = 404

match status:
    case 200:
        print("成功")
    case 400:
        print("错误请求")
    case 404:
        print("未找到")
    case 500:
        print("服务器错误")
    case _:
        print("未知状态码")
```

**类型匹配：**

```python
value = 3.14

match value:
    case int():
        print("整数")
    case float():
        print("浮点数")
    case str():
        print("字符串")
    case _:
        print("其他类型")
```

**结构化模式匹配：**

```python
point = (1, 2)

match point:
    case (0, 0):
        print("原点")
    case (0, y):
        print(f"Y轴上，y={y}")
    case (x, 0):
        print(f"X轴上，x={x}")
    case (x, y):
        print(f"点({x}, {y})")
    case _:
        print("不是二维点")
```

### 注意事项：

1. **浮点数比较**：

   ```python
   # 避免直接比较浮点数
   if 0.1 + 0.2 == 0.3:  # False
       pass
   
   # 应该使用
   if abs((0.1 + 0.2) - 0.3) < 1e-9:
       pass
   ```

2. **赋值与比较混淆**：

   ```python
   if x = 1:  # 错误，应该是 ==
       pass
   ```

3. **缩进错误**：

   ```python
   if condition:
   print("这会导致IndentationError")  # 错误
       print("正确缩进")  # 正确
   ```

###  练习

1. **成绩等级转换**

   ```python
   """
   	根据输入的成绩（0-100 的整数），输出对应的等级：
   	90+：A
   	80-89：B
   	70-79：C
   	60-69：D
   	60 以下：F
   	示例输入/输出：
   	输入: 85
   	输出: "B"
   """
   ```

2. **闰年判断**

   ```python
   """
   	判断输入的年份是否是闰年。闰年规则：
   		能被 4 整除但不能被 100 整除，或
   		能被 400 整除。
   	示例输入/输出：
   	输入: 2000
   	输出: "闰年"
   """
   ```

   

## 5. 流程控制语句

### 5.1 while

**在条件为真时重复执行代码块。**

```python
while 条件:
  条件满足时，执行语句
```

**example：**

```python
count = 1
while count <=100:
  print("hello,python!")
  count += 1
```

**注意事项：**

- while的条件需得到布尔类型，True表示继续循环，False表示结束循环
- 需要设置循环终止的条件，否则将无限循环
- 空格缩进和if判断一样，都需要设置

**练习**

```python
"""
	通过while循环，计算从1累加到100的和
"""
```

#### 5.1.1 猜数字案例

```python
"""
	设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
"""
```

#### 5.1.2 打印9*9乘法乘法表

```python
"""
1*2=2	2*2=4	
1*3=3	2*3=6	3*3=9	
1*4=4	2*4=8	3*4=12	4*4=16	
1*5=5	2*5=10	3*5=15	4*5=20	5*5=25	
1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36	
1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49	
1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64	
1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81	
"""
```

### 5.2 for

```python
for 临时变量 in 待处理的数据集:
  循环满足条件执行的语句
```

**示例：**

```python
str = "hello,world"

for s in str:
  print(s)
```

**注意事项：**

- **无法定义循环条件，只能被动取出数据处理**
- **要注意，循环内的语句，需要有空格缩进**

**练习**

```python
"""
	定义字符串'hello,world!hello,python!hello,java!'
	通过for循环，遍历此字符串，统计有多少个英文字母："o"
"""
```

#### 5.2.1. range

for循环语句，本质上是遍历：可迭代对象。

**range()**

获取一个从0开始，到num结束的数字序列（不含num本身）

range(5)取得的数据是：[0, 1, 2, 3, 4]

range(5, 10)取得的数据是：[5, 6, 7, 8, 9]

range(5, 10, 2)取得的数据是：[5, 7, 9]

```python
for i in range(5):
  print(i)
```

**练习**

```python
"""
	定义一个数字变量num，内容随意
	并使用range()语句，获取从1到num的序列，使用for循环遍历它。
	在遍历的过程中，统计有多少偶数出现
"""
```

#### 5.2.2 作用域

```python
for i in range(5):
  print(i)

print(i)  
```

如果在for循环外部访问临时变量：

- 实际上是可以访问到的
- 在编程规范上，是不允许、不建议这么做的

#### 5.2.3 嵌套使用

#####  打印9*9乘法乘法表

```python
"""
1*2=2	2*2=4	
1*3=3	2*3=6	3*3=9	
1*4=4	2*4=8	3*4=12	4*4=16	
1*5=5	2*5=10	3*5=15	4*5=20	5*5=25	
1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36	
1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49	
1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64	
1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81	
"""
```

#### 5.2.4 循环中断

**continue:**

continue关键字用于：中断本次循环，直接进入下一次循环

continue可以用于：  for循环和while循环，效果一致

**break:**

break关键字用于：直接结束所在循环

break可以用于：  for循环和while循环，效果一致

**else：**

循环正常结束时执行（未被 break 中断）

### 5.3 循环函数

#### 5.3.1 enumerate

**同时获取索引和值**

```python
fruits = "apple banana cherry"
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

#### 5.3.2 zip

**并行迭代多个序列**

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```



## 6. 函数

### 6.1 基础使用

**函数：**是组织好的，可重复使用的，用来实现特定功能的代码段

**好处：**

- 将功能封装在函数内，可供随时随地重复利用
- 提高代码的复用性，减少重复代码，提高开发效率

#### 6.1.1 基础语法

```python
def 函数名(传入参数):
  函数体
  return 返回值
# 调用函数
函数名(参数)
```

- 先定义函数
- 后调用函数
- 参数不需要，可以省略
- 返回值不需要，可以省略

**练习**

```python
"""
	定义一个函数，实现两数相加
"""
```

#### 6.1.2 None

Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>

无返回值的函数，实际上就是返回了：None这个字面量

None表示：空的、无实际意义的意思

```python
result = None
if not result:
  print("语句执行")
```

#### 6.1.3 作用域

变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）

主要分为两类：**局部变量**和**全局变量**

```python
num = 100

def test():
  num = 200
  
print(num)
test()
print(num)
```

**global**

```python
num = 100


def test():
    global num
    num = 200


print(num)
test()
print(num)
```

**练习**

```python
"""
	创建一个函数 is_prime(n)，判断输入的整数 n 是否是质数，返回布尔值
	（质数指在大于1的自然数中,除了1和它本身外无法被其他自然数整除的数）
"""
```



### 6.2 进阶使用

#### 6.2.1 多返回值

```python
def test1():
	return 1,2,3  # 多返回值，返回1，2，3

x,y,z = test1()  #通过x,y,z接收多个返回值->","分割

print(x,y,z)

def test2():
	return 1,"abc",True  # 多返回值，返回不同类型

x,y,z = test2()

print(x,y,z)
```

#### 6.2.2 多种参数使用

- **位置传参数**

  ```python
  def test_print(name, age, address):
  	print(f"姓名是:{name},年龄是:{age}, 住在: {address}")
  
  test_print("zhangsan",20,"四川省成都市")
  ```

- **关键字传参**

  ```python
  def test_print(name, age, address):
  	print(f"姓名是:{name},年龄是:{age}, 住在: {address}")
  
  test_print(age=20, address="四川省成都市", name="zhangsan")
  
  	# 位置参数和关键字参数混合使用，位置参数必须在前面
  test_print("zhangsan", age=20, address="四川省成都市")
  
  	# 位置参数和关键字参数混合使用，位置参数必须在前面
  test_print(name="zhangsan", age=20, "四川省成都市")  
  #SyntaxError: positional argument follows keyword argument
  ```

-  **缺省传参**

  ```python
  # 默认参数必须在非默认参数后面
  def test_print(name,address,age=18):
  	print(f"姓名是:{name},年龄是:{age}, 住在: {address}")
  
  
  test_print("zhangsan","四川省成都市",20)
  
  test_print("zhangsan","四川省成都市")
  
  ```

- **可变参数**

  ```python
  # 位置不定长
  def test_print(*args):
  	print(type(args)) # 元组类型
  	print(args)
  
  test_print(1,2,3,4,5,6,7)
  
  # 关键字不定长
  def test_print(**kwargs):
  	print(type(kwargs)) # 字典类型
  	print(kwargs)
  
  test_print(name="lisi",age=18)
  ```

- **函数作为参数**

  ```python
  def test_func(compute):
  	result = compute(1, 2)
  	print(type(compute))  # <class 'function'>
  	print(result)  # 3
  
  
  def compute(x,y):
  	return x + y
  
  
  test_func(compute)
  ```

#### 6.2.3 匿名函数

**lambad 传入参数:函数体(一行代码)**

```python
def test_func(compute):
	result = compute(1, 2)
	print(type(compute))
	print(result)

test_func(lambda x,y:x+y)  
test_func(lambda x,y:x-y)
```

### 6.3 闭包

**作用：**  **闭包可以保存函数内的变量，不会随着函数调用完而销毁**

**构成条件:**

- 在函数嵌套(函数里面再定义函数)的前提下

- 内部函数使用了外部函数的变量(还包括外部函数的参数)

- 外部函数返回了内部函数

```python
def func1(number):
    num = number
    def func2():
        result = 0
        result += num
        print(f'result:{result}')
    return func2


f = func1(20)
f()
f()
f()
```

#### 6.3.1 nonlocal

```python
def func1(number):
    num = number
    def func2():
        nonlocal  num
        num += 1
        print(f'result:{num}')
    return func2


f = func1(20)
f()
f()
f()
```

### 6.4 装饰器

**作用：在不改变原有函数的源代码的情况下,给函数增加新的功能**

**示例：**

```python
def test_dec(fn):
    def inner():
        print("执行方法前...")
        fn()
        print("执行方法后...")

    return inner

def func1():
    print("func1方法执行")

f = test_dec(func1)
f()
```

**简化：**

```python
def test_dec(fn):
    def inner():
        print("执行方法前...")
        fn()
        print("执行方法后...")

    return inner
@test_dec
def func1():
    print("func1方法执行")

func1()
```

**练习：**

```python
"""
	统计函数的执行时间 
		time.time()：获取当前时间戳
"""
```

#### 6.4.1 有参数的

```python
def test_dec(fn):
    def inner(a, b):
        fn(a, b)

    return inner


@test_dec
def func1(a, b):
    result = a + b
    print(result)


func1(1, 2)
```

#### 6.4.2 有返回值

```python
def test_dec(fn):
    def inner(a, b):
        return fn(a, b)
    return inner


@test_dec
def func1(a, b):
    result = a + b
    return result


print(func1(1, 2))

```

#### 6.4.3 不定长参数

```python
def test_dec(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)

    return inner


@test_dec
def func1(*args, **kwargs):
    print(f'args:{args},kwargs:{kwargs}')


func1(1, name='张三')

```

#### 6.4.4 多个装饰器

```python
def test_dec1(fn):
    def inner():
        print('test_dec1执行.....')
        fn()

    return inner


def test_dec2(fn):
    def inner():
        print('test_dec2执行.....')
        fn()

    return inner


@test_dec1
@test_dec2
def func1():
    print(f'func1执行...')


func1()

```

#### 6.4.5 装饰器有参数

```python
def outer(arg):
    def test_dec(fn):
        def inner():
            if arg == 'x':
                print('参数为x')
            else:
                print('参数不为x')
            print('test_dec1执行.....')
            fn()
        return inner
    return test_dec


@outer("a")
def func1():
    print(f'func1执行...')


func1()

```

**练习**

```python
"""
 	利用闭包/实现一个计数器
"""
```



## 7. 数据容器

**一种可以存储多个元素的Python数据类型**

### 7.1 列表

- **有序性**：元素按照插入顺序存储
- **可变性**：可以动态添加、删除或修改元素
- **异构性**：可以包含不同类型的元素
- **动态大小**：可自动扩展或收缩
- **可迭代**：支持迭代操作
- **可嵌套**：列表中可以包含其他列表

#### 7.1.1 定义语法

```python
list = ['abcd',10,'efg']

print(list)

print(type(list))  #. <class 'list'>
```

**列表内的每一个数据，称之为元素**

**列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套**

#### 7.1.2 列表的嵌套

```python
list = [['abcd',10],[123,456]]

print(list)

print(type(list))  #. <class 'list'>
```

#### 7.1.3 通过索引访问列表元素

```py
list1 = ['abcd',10,'efg']

print(list1[0])  #. abcd
print(list1[1])  #. 10
print(list1[2])  #. efg


print(list1[-3])  #. abcd
print(list1[-2])  #. 10
print(list1[-1])  #. efg


list2 = [['abcd',10],[123,456]]


print(list2[0])  #. ['abcd',10]
print(list2[1])  #. [123,456]
print(list2[0][0])  #. abcd
print(list2[0][1])  #. 10

print(list2[-2])  #. ['abcd',10]
print(list2[-1])  #. [123,456]
print(list2[-2][-2])  #. abcd
print(list2[-2][-1])  #. 10

```

#### 7.1.4 列表的常用方法

**查找指定元素在列表中的索引值**

```python
list = ['abcd',10,'efg']
index1 = list.index(10)
print(index1)


index2 = list.index(20)
print(index2)
```

**修改列表特定索引的值**

```python
list = ['abcd',10,'efg']

print(list[1])
list[1] = 20
print(list[1])
```

**插入元素**

```python
list = ['abcd',10,'efg']

print(list)
list.insert(1,50)
print(list)
```

**追加元素**

```pyth
list = ['abcd',10,'efg']

print(list)
list.append('aaa')
print(list)

list.extend(['bbb','ccc'])
print(list)
```

**删除索引对应元素**

```python
list = ['abcd',10,'efg']

print(list)
del list[1]
print(list)

item = list.pop(1)
print(list)
print(item)
```

**删除指定元素**

```python
list = ['abcd',10,'efg']

print(list)
list.remove('aaa')
print(list)
```

**清空列表**

```python
list = ['abcd',10,'efg']

print(list)
list.clear()
print(list)

```

**统计列表某元素个数**

```python
list = ['abcd',10,'efg',10]

count = list.count(10)
print(count)

# 删除一个10
list.remove(10)

count = list.count(10)
print(count)
```



**统计列表所有元素个数**

```python
list = ['abcd',10,'efg',20]

count = len(list)
print(count)

# 取出索引为1的元素
list.pop(1)

count = len(list)
print(count)
```

**练习**

```python
"""
	定义一个列表
	1.向列表尾部追加一个元素
	2.向列表尾部追加一个新的列表
	3.取出列表中的第二个元素，并输出
	4.取出列表的最后一个元素
	5.查找列表中某一个元素的对应下标索引
	6.统计列表所有元素个数并输出
"""
```

#### 7.1.5 遍历列表

```python
list = ['abcd',10,'efg',20]

#1. while
index = 0
while index < len(list):
  print(list[index])
  index += 1

#2. for
for item in list:
  print(item)
```

**练习	**

```python
"""
 1.定义一个列表，内容是[1,2,3,4,5,6,7,8,9,10]
 2.遍历列表，取出列表中的所有奇数，并存入一个新的列表中
 3.使用while循环和for循环各执行一次
"""
```

### 7.2 元组

**元组一旦定义完成，就不可修改**

- **不可变性**：创建后不能修改（不能添加、删除或修改元素）
- **有序性**：元素按照插入顺序存储
- **异构性**：可以包含不同类型的元素
- **可迭代**：支持迭代操作
- **可嵌套**：元组中可以包含其他元组或容器

#### 7.2.1 定义语法

```python
# 字面量
(1,2,3)
# 变量
tuple1 = (1,2,3)
print(tuple1)
print(type(tuple1))

# 空元组
tuple2 = ()
print(tuple2)
print(type(tuple2))

tuple3 = tuple()
print(tuple3)
print(type(tuple3))

# 定义单元素的元组
tuple4 = ("abc")
print(tuple4)
print(type(tuple4))

tuple5 = ("abc",)
print(tuple5)
print(type(tuple5))

# 嵌套
tuple6 = (("abc",1,2,3),(4,5,6))
print(tuple6)
print(type(tuple6))

```

#### 7.2.2 访问元组

```python
t1 = (("abc",1,2,3),(4,5,6))
print(t1[0][0])
```

#### 7.2.3 元组的常用方法

```python
t1 = (("abc",1,2,3,3,3,3,3),(4,5,6))

index = t1[0].index("abc")
print(index)

count = t1[0].count(3)
print(count)

length = len(t1)
print(length)
```

#### 7.2.4 遍历元组

```py
t1 = (("abc",1,2,3,3,3,3,3),(4,5,6))
# 1.while
index1 = 0
while index1 < len(t1):
    index2 = 0
    while index2 < len(t1[index1]):
        print(t1[index1][index2])
        index2 += 1
    index1 += 1
    
# 2.for    
for item1 in t1:
    for item2 in item1:
        print(item2)    
```

#### 7.2.5 修改元组元素

```python
t1 = (1,2,3,['abc','efg'])
# 不可以直接修改元组内的元素
t1[0] = 3

# 可以修改元组内部list中的元素
t1[3][0] = 'aaa'

print(t1)
```

**练习**

```python
"""
	定义一个元组 内容是('小明',11,['唱歌'，'跳舞'])，记录的是姓名，年龄，爱好ß
	1.查询其年龄的下标索引位置
	2.输出学生的姓名
	3.删除唱歌，跳舞其中一个爱好
	4.增加一个'coding'爱好
"""
```

### 7.3 字符串

- **不可变性**：创建后不能修改，任何修改操作都会创建新字符串
- **有序性**：字符按顺序存储，支持索引和切片

#### 7.3.1 定义语法

```python
str = "hello world"
print(str[0])   # h
print(str[-10]) # h

# 从其他类型转换
num_str = str(123)  # '123'
bool_str = str(True)  # 'True'

# 创建空字符串
empty = str()
```

**字符串不能进行修改**

```python
str = "hello world"
str[0] = "a"
```

#### 7.3.2 字符串的常用方法

- ```python
  str1 = "hello world"
  
  # in 运算符
  print("hello" in str1)  # True
  
  
  index = str1.index("hello")
  print(index)  # 0	
  
  # find() 方法（返回索引，找不到返回-1）
  print(str1.find("hello"))  # 0
  print(str1.find("Java"))  # -1
  
  str2 = "abcabcabcabc"
  new_str2 = str2.replace("abc","bbb") # 不是修改字符串，而是得到一个新的字符串
  print(str2)
  print(new_str2)
  
  str3 = "hello world hello python"
  new_list = str3.split(" ") # 字符串本身不变，按照指定的分隔符得到一个新的列表对象
  print(str3)
  print(new_list)
  print(type(new_list))
  
  
  str4 = " hello world "
  print(str4.strip()) # 空参去除首尾空格
  
  str5 = "abhello worldbba"
  print(str5.strip("ab")) # 去除首尾"a","b"字符
  
  print(str1.count("l")) # 统计"l"出现的次数
  
  print(len(str1)) # 统计字符串的长度
  
  
  
  ```

**练习**

```python
"""
 定义一个字符串str = "12hello python,hello world,hello java12"
 1.使用for循环和while遍历字符串，并输出每一个字符
 2.统计字符串内有多少个"hello"
 3.使用方法处理字符串，得到列表['hello python', 'hello world', 'hello java']
"""
```

### 7.4 序列

**序列:** 内容连续、有序、可使用下标索引的一类数据容器

- **列表**

- **元组**

- **字符串**

#### 7.4.1 切片

**切片:** 从一个序列中，取出一个子序列

**语法: **序列[起始下标:结束下标:步长]

- `start`：切片开始位置（包含），默认为0
- `stop`：切片结束位置（不包含），默认为序列长度
- `step`：步长（可选），默认为1

#### 7.4.2 切片的常用方法

```python
list = [0,1,2,3,4,5,6,7]
new_list1 = list[1:4] # 步长默认为1
print(new_list1) # [1,2,3]

tuple = (0,1,2,3,4,5,6,7)
new_tuple1 = tuple[:] # 起始和结束不写表示从头到尾
print(new_tuple1) # (0,1,2,3,4,5,6,7)

str = "01234567"
new_str1 = str[::2]
print(new_str1) # 0246

new_str2 = str[::-1]
print(new_str2) # 76543210

new_list2 = list[3:1:-1]
print(new_list2) # [3,2]

new_tuple2 = tuple[::-2]
print(new_tuple2) # (7,5,3,1)

```

**练习**

```python
"""
 定义一个字符串"avaj olleh,nohtyp olleh"
 1.使用学到的方法得到字符串"hello python"
"""
```

### 7.5 集合

- **无序性**：元素没有固定顺序
- **唯一性**：自动去除重复元素
- **高效性**：基于哈希表实现，查找、添加、删除操作平均时间复杂度为 O(1)
- **可变性**：可以动态添加、删除元素

#### 7.5.1 定义语法

```python
set1 = {"abc",123,456,123}
print(set1)

set2 = set()
print(set2)
print(type(set2))
```

#### 7.5.2 常用操作

```python
set = {"abc","efg"}
print(set)

# 添加新元素
set.add("abc")
set.add(123)
print(set)

# 移除元素
set.remove("abc")
print(set)

# 随机取出元素,集合本身被修改，取出的元素被删除
item = set.pop()
print(set)
print(item)

# discard() - 删除指定元素，元素不存在不报错
set.discard(10)  # 无变化


# 清空集合
set.clear()
print(set)
```

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 并集
print(A | B)   # {1, 2, 3, 4, 5, 6}
print(A.union(B))

# 交集
print(A & B)   # {3, 4}
print(A.intersection(B))

# 差集
print(A - B)   # {1, 2}
print(A.difference(B))

# 对称差集（仅在A或仅在B中的元素）
print(A ^ B)   # {1, 2, 5, 6}
print(A.symmetric_difference(B))
```

#### 7.5.3 遍历集合

```python
set = {1,2,3,4}

for item in set:
  print(item)
```

**练习**

```python
"""
 定义一个列表对象list = ["a","a","b","b","c","c",1,2,3,1]
 1.定义一个空集合
 2.通过for循环遍历列表，将列表中的元素添加到空集合中
 3.打印输出集合
"""
```

### 7.6 字典

- **无序性**：Python 3.6+ 字典保持插入顺序，但本质上仍是无序集合
- **键唯一性**：每个键必须是唯一的
- **键不可变性**：键必须是不可变类型(如字符串、数字、元组)
- **动态性**：可随时添加、修改、删除键值对
- **高效性**：查找、插入、删除操作的平均时间复杂度为 O(1)

#### 7.6.1 定义语法

```python
dict1 = {"name":"zhangsan","age":17,"score":80}
print(dict1)
print(type(dict)
      
# 定义空字典
dict2 = dict()
dict3 = {}
print(type(dict2))
print(type(dict3))

# key不可以重复  
dict2 = {"name":"zhangsan","age":17,"score":80，"score":88}
print(dict2)
# 通过key获取value
print(dict2["name"])
print(dict2["age"])
```

#### 7.6.2 字典的嵌套

```python
# key不能为字典类型
score_dict = {
  						"zhangsan":{"math":90,"english":92},
              "lisi":{"math":60,"english":59}
             }
print(score_dict["zhangsan"])
print(score_dict["zhangsan"]["english"])
```

#### 7.6.3 字典的常用方法

```python
score_dict = {"zhangsan":90,"lisi":80}
print(score_dict)

# 新增元素
score_dict["wangwu"] = 99
print(score_dict)

# 修改元素
score_dict["lisi"] = 100
print(score_dict)

# 删除元素
value = score_dict.pop("zhangsan")
print(value)
print(score_dict)

# 清空字典
score_dict.clear()
print(score_dict)

#获取全部的key
score_dict = {"zhangsan":90,"lisi":80}
keys = score_dict.keys()
print(keys)


#统计字典内的元素数量
length = len(score_dict)
print(length)

#检查键是否存在
print('zhangsan' in score_dict)
```

#### 7.6.4 遍历字典

```python
score_dict = {"zhangsan":90,"lisi":80}
# 方式1
keys = score_dict.keys()
for key in keys:
  print(score_dict[key])

# 方式2
for key in score_dict:
  print(score_dict[key])
```

**练习**

|   姓名   | 年龄 | 地址         | 邮箱                  |
| :------: | ---- | ------------ | --------------------- |
| Zhangsan | 23   | 四川省成都市 | 12345678910@gmail.com |
|   Lisi   | 22   | 四川省绵阳市 | 12345678910@gmail.com |
|  Wangwu  | 21   | 四川省眉山市 | 12345678910@gmail.com |

```python
"""
	通过上述表格定义对应的字典内容并输出:
	zhangsan:{'age': 23, 'address': '四川省成都市', 'email': '12345678910@gmail.com'}
	lisi:{'age': 22, 'address': '四川省绵阳市', 'email': '12345678910@gmail.com'}
	wangwu:{'age': 21, 'address': '四川省眉山市', 'email': '12345678910@gmail.com'}
	1.修改zhangsan的年龄为19
	2.添加姓名为->zhaoliu,年龄->20，地址->湖北省武汉市，邮箱->12345678911@gmail.com
	3.删除字典中姓名为wangwu的元素
"""
```

## 8. 文件

**常用模式**：

- `'r'`：只读（默认）
- `'w'`：写入（会覆盖已有文件）
- `'a'`：追加
- `'x'`：独占创建（文件已存在则失败）
- `'b'`：二进制模式
- `'t'`：文本模式（默认）
- `'+'`：读写模式

### 8.1 读取文件

<iframe src="./file/1.txt" width="100%" height="100px"></iframe>

```python
f = open('../file/1.txt', 'r', encoding='utf-8')

print(type(f))

print(f.read(4)) #读取4个字节 床前明月

print(f.read()) 
"""
接着读取剩下的内容:
光
疑是地上霜
举头望明月
低头思故乡
"""

lines = f.readlines()  # 读取全部行
print(type(lines))     # <class 'list'>
print(lines) 

#读取一行
line = f.readline()
print(line)

# for循环读取文件
for line in f:
  print(line)
```

### 8.2 关闭文件

```python
f = open('../file/1.txt', 'r', encoding='utf-8')

#读取一行
line = f.readline()
print(line)

f.close()
time.sleep(5000000)
```

### 8.3 with open

```python
with open('../file/1.txt', 'r', encoding='utf-8') as f:
  for line in f:
    print(line) #自动执行close方法
```

**练习**

<iframe src="./file/2.txt" width="100%" height="100px"></iframe>

```python
"""
 1.读取上述文件的内容
 2.统计字符'a'出现的次数
"""
```

### 8.4 写入文件

```python
# 文件不存在则创建
f = open('../file/test.txt', 'w', encoding='utf-8')

f.write("hello,world")
# 将内容写入到磁盘中
f.flush()
```

```python
# 打开一个已存在的文件
f = open('../file/test.txt', 'w', encoding='utf-8')

f.write("hello,python")
f.close() #自动执行flush方法
```

**练习**

**1.保存用户输入的内容**

```python
"""
	将用户输入的多行文本保存到一个文件中（例如 output.txt）。
	用户可以输入多行内容，输入 exit 时结束输入
	示例内容:
	请输入内容（输入 exit 结束）:
> Hello, world!
> This is a test.
> exit
生成的文件 (output.txt):
Hello, world!
This is a test.
"""
```

**2. 统计文件中单词的出现次数**

```python
"""
 读取一个文本文件（例如 text.txt），统计文件中每个单词的出现次数，并将结果写入另一个文件
 示例文件内容 (text.txt):
 Hello world!
 Hello Python.
 Python is great.
 生成的文件 (word_count.txt):
 Hello: 2
 world: 1
 Python: 2
 is: 1
 great: 1
"""
```

**3. 文件加密和解密**

```python
"""
 实现简单的文件加密和解密功能。加密规则可以是将每个字符的 ASCII 码加 1
 解密规则则是将每个字符的 ASCII 码减 1。
 示例文件内容 (secret.txt):
 Hello, world!
 加密后的文件 (encrypted.txt):
 Ifmmp-!xpsme"
 解密后的文件 (decrypted.txt):
 Hello, world!
"""
```



### 8.5 追加写入

```python
f = open('../file/test.txt', 'a', encoding='utf-8')

f.write("\nhello,world")
# 将内容写入到磁盘中
f.flush()
```

**练习**

**1. 追加统计文件中单词的出现次数** 

```python
"""
 在上述原有的word_count.txt文件中追加统计新文件夹中的单词数量
 新文件夹内容(new_text.txt):
 Network security!
 Java Sql!
 Java Web.
 Network security!
 追加写入后word_count.txt:
 Hello: 2
 world: 1
 Python: 2
 is: 1
 great: 1
 Network: 2
 security: 2
 Java: 2
 Sql: 1
 Web: 1
"""
```

### 8.6 文件位置操作

#### 获取当前位置

```python
with open('1.txt', 'r') as f:
    pos = f.tell()  # 返回当前文件指针位置
```

#### 移动文件指针

```python
with open('1.txt', 'r') as f:
    f.seek(10)  # 移动到第10字节
    f.seek(5, 1)  # 从当前位置移动5字节
    f.seek(-3, 2)  # 从文件末尾向前移动3字节
```

**seek() 参数**：

- `offset`：移动的字节数
- `whence`（可选）：
  - `0`：从文件开头（默认）
  - `1`：从当前位置
  - `2`：从文件末尾

### 8.7 文件的二进制操作

`处理图片、音频等非文本文件：`

```python
# 复制二进制文件
with open('source.jpg', 'rb') as src, open('copy.jpg', 'wb') as dst:
    dst.write(src.read())
```

### 8.8 常用文件操作函数

#### 文件系统操作

```python
import os

# 检查文件/目录是否存在
os.path.exists('file.txt')

# 获取文件大小
os.path.getsize('file.txt')

# 重命名文件
os.rename('old.txt', 'new.txt')

# 删除文件
os.remove('file.txt')
```

#### 目录操作

```python
import os

# 列出目录内容
os.listdir('/path/to/dir')

# 创建目录
os.mkdir('new_dir')

# 递归创建目录
os.makedirs('path/to/new/dir')

# 删除空目录
os.rmdir('empty_dir')
```

### 注意事项：

1. **总是使用 `with` 语句**：确保文件正确关闭
2. **处理大文件时**：使用逐行或分块读取
3. **检查文件是否存在**：操作前先验证
4. **处理不同编码**：指定正确的编码（如 `encoding='utf-8'`）
5. **异常处理**：捕获可能的IOError/OSError

## 9. 异常

- **定义**：异常是程序执行过程中发生的错误或意外情况。

- **示例**：

  ```python
  result = 10 / 0  # ZeroDivisionError
  ```

- **异常的作用**：帮助开发者定位和处理错误，避免程序崩溃。

### 9.1 捕获异常

#### 9.1.1 基础使用

```python
try:
  # 读取一个不存在的文件
  f = open('../file/3.txt', 'r', encoding='utf-8')
  print("测试这条语句是否执行...")
except:
  # 出现异常执行的操作
  print("出现异常,输出这条语句...")
```

#### 9.1.2 捕获指定异常

- **指定异常**

```python
try:
	result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e: 
  print(e)
```

- **多个指定异常**

```python
try:
  f = open('../file/3.txt', 'r', encoding='utf-8')
except (ZeroDivisionError,FileNotFoundError) as e:
  print(e)
```

- **所有异常**

```python
try:
	print(name)
except Exception as e: 
  print(e)
```

### 9.2 异常可选操作

- **else**

```python
try:
	result = 10 / 1  # 正常执行
except ZeroDivisionError as e: 
  print(e)
else:
  print("没有异常，执行这条语句")
```

- **finally**

```python
#1. 无异常finally执行
try:
	result = 10 / 1  # 正常执行
except ZeroDivisionError as e: 
  print(e)
else:
  print("没有异常，执行这条语句")
finally:
  print("一定会执行")

#2. 有异常finally执行  
try:
	result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e: 
  print(e)
else:
  print("没有异常，执行这条语句")
finally:
  print("一定会执行")
```

### 9.3 异常的传递性

```python
def func1():
    print("func1开始执行")
    print(name)
    print("func1结束执行")


def func2():
    print("func2开始执行")
    func1()  # 调用func1方法
    print("func2结束执行")


def main():
    try:
        func2()  # 调用func2方法
    except Exception as e:
        print("出现异常",e)

main()
```

### 9.4 raise

`raise`是用于**显式引发异常**的关键字

#### 基本用法

#### 1. 引发内置异常

```python
raise ValueError("这是一个错误消息")
```

这会立即引发一个 `ValueError` 异常，并附带指定的错误消息。

#### 2. 重新引发当前处理的异常

在 `except` 块中，可以不带参数使用 `raise` 来重新引发当前正在处理的异常：

```python
try:
    # 可能出错的代码
    x = 1 / 0
except ZeroDivisionError:
    print("捕获到除零错误")
    raise  # 重新引发相同的异常
```

#### 3. 从异常链中引发新异常

`from` 关键字来保留原始异常信息

```python
try:
    x = 1 / 0
except ZeroDivisionError as original_error:
    raise ValueError("转换错误") from original_error
```

**这会显示两个异常，表明新异常是由原始异常引起的。**

### 主要作用

1. **主动触发异常**：当程序检测到错误条件时，可以主动抛出异常
2. **异常传递**：在异常处理中重新抛出异常，让上层调用者处理
3. **自定义异常**：与自定义异常类配合使用，创建特定的错误处理机制
4. **调试辅助**：在开发过程中强制引发异常以测试错误处理逻辑



## 10. 模块

- 模块是一个包含 Python 代码的 `.py` 文件
- 可以包含函数、类、变量和可执行代码
- 模块名就是文件名去掉 `.py` 后缀

### 10.1 基础使用

**import**  模块名

```python
# 导入time模块
import time

print('开始执行....')
time.sleep(10) #睡眠10s
print('结束执行....')
```

**from** 模块名 **import** 功能名

```python
# 导入time模块中的sleep方法
# from time import sleep

#导入time模块中的所有功能
from time import * 

print('开始执行....')
sleep(10) #睡眠10s
print('结束执行....')
```

**as** 别名

```python
import time as tt #取别名为tt

tt.sleep(10)
print("结束执行")
```

```python
from time import sleep as sp

sp(10)
print("结束执行")
```



### 10.2 内置模块 json

|  **函数**  | **描述**                                 |
| :--------: | ---------------------------------------- |
| json.dumps | 将 Python 对象编码成 JSON 字符串         |
| json.loads | 将已编码的 JSON 字符串解码为 Python 对象 |
|            |                                          |

```python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

data2 = json.dumps(data)  
print(data2)  # [{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]



jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

```



### 10.3 自定义模块

<img src="./images/模块1.png" alt="image-20250313171833326" style="zoom:33%;" />

```python
# 导入自定义模块
import my_module

# 使用自定义模块中的功能
result = my_module.add(1,2)

print(result)
```

#### 10.3.1 注意事项

- **导入不同模块相同的函数名**

![](./images/模块2.png)

```python
from test_module1 import test

from test_module2 import test


test()
# module2 test方法执行...
```

- **变量main,all**

![](./images/模块3.png)

```python
import my_module

# 直接调用会执行my_module模块中的add方法
```

**name**

- 当模块被直接运行时，`__name__` 等于 `"__main__"`
- 当模块被导入时，`__name__` 等于模块名

```python
def add(a, b):
    print(a + b)
    return a + b

if __name__ == '__main__':
    add(1, 2)
```

**all**

- 控制`from xxx import *` 的行为

<img src="./images/模块4.png" style="zoom:50%;" />

```python
from  my_module import * # all 变量限制import*时哪些功能能被导入

add(1,2)
sub(1,2) # sub函数不能调用
```

### 10.4 包

- 包是包含多个模块的目录
- 必须包含 `__init__.py` 文件(可以是空文件)
- 允许嵌套(子包)

**安装包**

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

#### 示例

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
```

#### 基础使用

```python
import pymysql
from pymysql.cursors import DictCursor

con = pymysql.Connection(host='43.139.213.136', port=3306,
                         user='user', password='admin123456',
                         cursorclass=DictCursor)

con.select_db('test')

cursor = con.cursor()

sql = 'select * from student'

cursor.execute(sql)

result = cursor.fetchall()

for r in result:
    print(r)
```



## 11. 对象

对象是类的实例化结果，它是一个具体的数据实体，包含了：

- **数据（属性）**：对象的状态或特征。

- **行为（方法）**：对象可以执行的操作或功能。

  

例如：

- 数字 `5` 是一个整数对象。
- 字符串 `"hello"` 是一个字符串对象。
- 列表 `[1, 2, 3]` 是一个列表对象。

**特性：**

1. **身份（Identity）**：
   - 每个对象都有一个唯一的标识符（ID），可以通过 `id()` 函数获取。
   - 例如：`id(5)` 会返回一个唯一的整数，表示对象 `5` 的内存地址。
2. **类型（Type）**：
   - 对象的类型决定了它可以存储什么数据，以及可以执行什么操作。
   - 可以通过 `type()` 函数获取对象的类型。
   - 例如：`type("hello")` 返回 `<class 'str'>`，表示这是一个字符串对象。
3. **值（Value）**：
   - 对象的具体数据内容。
   - 例如：字符串对象 `"hello"` 的值是字符序列 `h`, `e`, `l`, `l`, `o`。
4. **属性（Attributes）**：
   - 对象可以包含数据属性（变量）和方法属性（函数）。
   - 例如：列表对象 `[1, 2, 3]` 有 `append()` 方法。
5. **方法（Methods）**：
   - 方法是与对象关联的函数，用于操作对象的数据。
   - 例如：字符串对象 `"hello"` 有 `upper()` 方法，可以将字符串转换为大写。

### 11.1 定义语法

```python
# 定义一个学生类
class Student:
    age = None
    name = None
    gender = None
```

Python 提供了许多内置对象类型，例如：

- **数字**：`int`, `float`, `complex`
- **字符串**：`str`
- **列表**：`list`
- **元组**：`tuple`
- **字典**：`dict`
- **集合**：`set`
- **布尔值**：`bool`
- **文件**：`file`
- **函数**：`function`
- **模块**：`module`

### 11.2 成员方法

```python
# 定义一个学生类
class Student:
  # 成员属性
    age = None
    name = None
    gender = None
		# 成员方法
    def info(self):
        print(f"学生的姓名:{self.name},学生的年龄:{self.age},学生的性别:{self.gender}")

# 创建一个学生对象
stu1 = Student()

stu1.name = "zhangsan"
stu1.age = 20
stu1.gender = "男"

print(stu1.age)

stu1.info()
```

### 11.3 类和对象

```python
class Clock:
  id = None
  price = None
  
  def ring(self):
    import winsoud
    winsoud.ring(2000,3000)
    
clock = Clock()
clock.ring()
```

### 11.4 构造方法

```python
class Student:
  # 构造方法init
    def __init__(self, name, age):
        self.name = name
        self.age = age



stu = Student("John", 18)
print(stu.age)
```

**练习**

```python
"""
	设计一个学生类，记录学生的姓名，年龄，联系方式
	1.通过循环，配合input输入语句，完成对5个学生对象录入并创建
	2.打印输出所有的学生对象
	
"""
```

### 11.5 魔术方法

魔术方法（Magic Methods），也称为特殊方法或双下方法（Dunder Methods），是 Python 中以双下划线开头和结尾的特殊方法。

- 以双下划线开头和结尾的方法（如 `__init__`）
- Python 在特定情况下自动调用这些方法
- 用于实现运算符重载、对象行为定制等功能

#### 11.5.1 构造与初始化

- `__new__(cls[, ...])`: 创建实例时首先调用的方法（类方法）
- `__init__(self[, ...])`: 实例初始化方法（最常用的魔术方法）
- `__del__(self)`: 对象销毁时调用

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        print("Initializing instance")
        self.value = value
    
    def __del__(self):  #析构方法
        print("Deleting instance")

obj = MyClass(10)  # 输出: Creating instance, Initializing instance
del obj            # 输出: Deleting instance
```

#### 11.5.2. 字符串表示

- `__str__(self)`: 定义 `str(obj)` 和 `print(obj)` 的输出
- `__repr__(self)`: 定义 `repr(obj)` 和交互式解释器的输出
- `__format__(self, format_spec)`: 定义 `format()` 和 f-string 的行为

__str__

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __format__(self, format_spec):
        if format_spec == 'r':
            return f"({self.y}, {self.x})"
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(str(p))      # Point(3, 4)
print(repr(p))     # Point(x=3, y=4)
print(f"{p}")      # (3, 4)
print(f"{p:r}")    # (4, 3)
```

#### 11.5.3 比较运算符

- `__eq__(self, other)`: `==`
- `__ne__(self, other)`: `!=`
- `__lt__(self, other)`: `<`
- `__le__(self, other)`: `<=`
- `__gt__(self, other)`: `>`
- `__ge__(self, other)`: `>=`

__lt__ (<)

```python
class Student:
    # 构造方法init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名:{self.name},年龄:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

stu1 = Student("John", 18)
stu2 = Student("Ann", 20)
print(stu1 > stu2)
print(stu1 < stu2)
```

__le__(<=)

```python
class Student:
    # 构造方法init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名:{self.name},年龄:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

stu1 = Student("John", 20)
stu2 = Student("Ann", 20)
print(stu1 >= stu2)
print(stu1 <= stu2)
```

__eq__(==)

```python
class Student:
    # 构造方法init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名:{self.name},年龄:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("John", 20)
stu2 = Student("Ann", 20)
print(stu1 == stu2)

```

#### 11.5.4 上下文管理

- `__enter__(self)`: 进入 `with` 语句块时调用
- `__exit__(self, exc_type, exc_val, exc_tb)`: 退出 `with` 语句块时调用

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.2f} seconds")
    


with Timer() as t:
    # 执行一些操作
    sum(range(1000000))
```



### 11.6 私有化

`私有化`是一种封装机制，用于限制对类内部属性和方法的直接访问。Python 通过命名约定和一些特殊语法来实现不同程度的私有化

```python
class Student:
	age = 20
  __tel = '10086'
  
  def print_tel(self):
    print(self.__tel)
```

### 11.7 封装

####  1.封装的核心思想

- **隐藏实现细节**：将对象的属性和方法隐藏在内部，外部无法直接访问。
- **暴露必要接口**：通过公共方法（接口）来访问或修改对象的内部状态。
- **提高安全性**：防止外部代码随意修改对象的内部数据，确保数据的完整性。

------

#### **2. 访问控制**

Python 通过命名约定来实现访问控制，而不是像其他语言（如 Java）那样通过关键字（如 `private`、`protected`）来实现。

#### **命名约定**

- **公共成员（Public）**：
  - 名称没有任何前缀。
  - 可以在类的外部直接访问。
  - 例如：`self.name`。
- **受保护成员（Protected）**：
  - 名称以单下划线 `_` 开头。
  - 这是一种约定，表示该成员仅供类内部或子类使用，但外部仍然可以访问。
  - 例如：`self._age`。

- **私有成员（Private）**：
  - 名称以双下划线 `__` 开头。
  - Python 会对名称进行名称修饰（Name Mangling），使得外部无法直接访问。
  - 例如：`self.__salary`。

```python
class Person:
    def __init__(self, name, age, salary):
        self.name = name       # 公共属性
        self._age = age        # 受保护属性
        self.__salary = salary # 私有属性

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

# 创建对象
person = Person("Alice", 30, 50000)

# 访问公共属性
print(person.name)  # 输出: Alice

# 访问受保护属性（不推荐，但可以访问）
print(person._age)  # 输出: 30

# 访问私有属性（会报错）
# print(person.__salary)  # 报错: AttributeError

# 通过公共方法访问私有属性
person.display_info()  # 输出: Name: Alice, Age: 30, Salary: 50000
```

####  **3. 属性管理**

Python 提供了 `@property` 装饰器，用于将方法转换为属性，从而实现对属性的精细控制。

##### **使用 `@property` 的好处**

- 可以在访问或修改属性时添加额外的逻辑（如数据验证）。
- 保持接口的一致性，外部代码无需知道属性是直接存储还是通过计算得到的。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    @property
    def age(self):  # 获取属性
        return self._age

    @age.setter
    def age(self, value):  # 设置属性
        if value < 0:
            raise ValueError("年龄不能为负数")
        self._age = value

# 创建对象
person = Person("Bob", 25)

# 访问属性
print(person.age)  # 输出: 25

# 修改属性
person.age = 30
print(person.age)  # 输出: 30

# 尝试设置非法值
# person.age = -10  # 报错: ValueError: 年龄不能为负数
```

1. **`@property` 方法**：
   - `age` 方法被 `@property` 装饰，使得 `age` 成为一个只读属性。
   - 可以通过 `stu1.age` 访问 `__age` 的值。
2. **`@age.setter` 方法**：
   - `age` 方法被 `@age.setter` 装饰，使得 `age` 成为一个可写属性。
   - 可以通过 `stu1.age = value` 修改 `__age` 的值。
   - 在设置值时，会检查 `value` 是否为负数，如果是负数则抛出 `ValueError`。
3. **封装性**：
   - `__age` 是私有属性，外部代码不能直接访问或修改。
   - 通过 `@property` 和 `@age.setter`，外部代码可以安全地访问和修改 `age`。

### 11.8 继承

`继承`是面向对象编程的三大特性之一，它允许我们定义一个类（子类）来继承另一个类（父类）的属性和方法

#### 11.8.1 单继承

```python
class Person:
    name = None
    age = None

    def say_hi(self):
        print("Hello,world!")

class Student(Person):
    tel = None


stu = Student()
stu.age = 20
stu.name = ("lisi")
print(stu.age)
print(stu.name)
stu.say_hi()
```

#### 11.8.2 多继承

```python
class Father:
    def father_method(self):
        return "Father's method"

class Mother:
    def mother_method(self):
        return "Mother's method"

class Child(Father, Mother):
    pass

child = Child()
print(child.father_method())  # "Father's method"
print(child.mother_method())  # "Mother's method"
```

**注意事项**

- **父类中有同名方法或属性**

  ```python
  class Person:
      name = "Person"
      age = None
  
      def say_hi(self):
          print("Hello,world!")
  
  class Student(Person):
      name = "Student"
      tel= None
  
  class NewStudent(Student, Person):
      pass
  
  stu = NewStudent()
  print(stu.name) # 输出什么？
  ```

- **pass**

  **占位语句，表示语句的完整性**

#### 11.8.3 复写

```python
class Person:
    name = "Person"
    age = None
    def say_hi(self):
        print("Hello,world!")

class Student(Person):
  # 复写父类的成员属性
    name = "Student"
    # 复写父类的成员方法
    def say_hi(self):
        print("Hello,python!")
        print("Hello,world!")
        print("Hello,java!")

 
```

**调用父类的成员属性，方法**

1. ```python
   class Person:
       name = "Person"
       age = None
       def say_hi(self):
           print("Hello,world!")
   
   class Student(Person):
       name = "Student"
   
       def say_hi(self):
           print("Hello,python!")
           print(Person.name)
           print(self.name)
           Person.say_hi(self)
           print("Hello,java!")
   
   
   stu = Student()
   stu.say_hi()
   ```

2. ```python
   class Person:
       name = "Person"
       age = None
       def say_hi(self):
           print("Hello,world!")
   
   class Student(Person):
       name = "Student"
   
       def say_hi(self):
           print("Hello,python!")
           print(super().name)
           print(self.name)
           super().say_hi()
           print("Hello,java!")
   
   
   stu = Student()
   stu.say_hi()
   ```

### 11.9 类型注解

#### 11.9.1 基础语法

**变量：类型**

```python
name:str = "zhangsan"
age:int = 18
class Student:
  pass
# 类对象
stu:Student = Student()

# 容器
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {"name":"lisi"}

my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool] = (1,"abc",True)
my_dict:dict[str,str] = {"name":"lisi"}

# 注释中使用类型注解
name = "zhangsan" # type:str
age:int = 18      # type:int
```

#### 11.9.2 函数和方法

```python
def add(x:int,y:int):
  return x+y

result = add(1,2)
print(result)

# 返回值
def sub(x:int,y:int) -> int:
  return x - y
print(sub(2,1))
```

#### 11.9.3 union

```python
from typing import Union


my_list:list[Union[int,str]] = [1, "abc", 3]

my_dict:dict[str, Union[int,str]] = {"a":1, "b":2, "c":3}
```

### 11.10 多态

`多态`是指同一个方法调用由于对象不同可能会产生不同的行为。

#### 11.10.1 继承多态

通过方法重写实现多态

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal: Animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # "Woof!"
animal_sound(cat)  # "Meow!"
```

#### 11.10.2 鸭子类型(Duck Typing)

Python特色的多态实现方式，不依赖继承关系

[详细介绍]: https://baijiahao.baidu.com/s?id=1810792470054393286

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_it_quack(thing):
    print(thing.quack())

duck = Duck()
person = Person()

make_it_quack(duck)    # "Quack!"
make_it_quack(person)  # "I'm quacking like a duck!"
```

### 11.11 静态方法

静态方法使用 `@staticmethod` 装饰器定义：

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        print(f"静态方法调用: args={arg1}, {arg2}")
        
# 调用方式
MyClass.static_method(1, 2)  # 通过类调用
obj = MyClass()
obj.static_method(1, 2)     # 通过实例调用
```

特点：

- **不接收**隐式的第一个参数（没有 `self` 或 `cls`）
- 不能访问实例属性或其他实例方法（因为它没有 `self`）
- 也不能访问类属性或类方法（因为它没有 `cls`）
- 可以通过类或实例调用
- 本质上就是一个普通函数，只是放在类的命名空间中

使用场景：

- 当方法逻辑上属于类，但不需要访问类或实例的任何属性时
- 作为工具函数使用
- 组织相关功能到类的命名空间下

### 11.12 类方法

类方法使用 `@classmethod` 装饰器定义：

```python
class MyClass:
    class_attribute = "类属性"
    
    @classmethod
    def class_method(cls, arg1, arg2):
        print(f"类方法调用: cls={cls}, args={arg1}, {arg2}")
        print(f"可以访问类属性: {cls.class_attribute}")
        
# 调用方式
MyClass.class_method(1, 2)  # 通过类调用
obj = MyClass()
obj.class_method(1, 2)     # 通过实例调用
```

特点：

- 第一个参数是 `cls`，指向类对象（不是实例）
- 可以访问类属性和其他类方法
- 不能访问实例属性（除非通过实例参数）
- 可以通过类或实例调用
- 当通过实例调用时，`cls` 仍然是类对象而非实例

使用场景：

- 需要访问或修改类状态时（类属性）
- 作为工厂方法创建类的实例
- 实现替代构造函数（多态构造函数）

| 特性         | 实例方法           | 类方法               | 静态方法      |
| :----------- | :----------------- | :------------------- | :------------ |
| 装饰器       | 无                 | @classmethod         | @staticmethod |
| 第一个参数   | self (实例)        | cls (类)             | 无            |
| 访问实例属性 | 可以               | 不可以               | 不可以        |
| 访问类属性   | 通过self.**class** | 可以直接访问         | 不可以        |
| 调用方式     | 必须通过实例       | 类或实例             | 类或实例      |
| 主要用途     | 操作实例数据       | 操作类数据或工厂方法 | 工具函数      |

#### 使用场景

##### 静态方法示例

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# 使用
print(MathUtils.add(5, 3))  # 8
print(MathUtils.multiply(5, 3))  # 15
```

##### 类方法示例 - 工厂方法

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])
    
    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

# 使用工厂方法创建不同种类的披萨
margherita = Pizza.margherita()
prosciutto = Pizza.prosciutto()
```

##### 类方法示例 - 替代构造函数

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def from_timestamp(cls, timestamp):
        import time
        date = time.localtime(timestamp)
        return cls(date.tm_year, date.tm_mon, date.tm_mday)

# 使用不同的构造方式
d1 = Date(2023, 5, 15)
d2 = Date.from_string("2023-05-15")
d3 = Date.from_timestamp(1684147200)
```



### 学生管理系统

```python
"""
		实现一个学生管理系统，要求学生有学号、姓名、年龄、性别信息
		1.实现添加学生功能
		2.实现删除学生功能
		3.实现查找学生功能
		4.实现修改学生功能
		5.退出系统
"""

```

```python
class Student:
    def __init__(self, id, age, name):
        self.id = id
        self.__age = age
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f"姓名:{self.__name}, 年龄:{self.age}, 学号:{self.id}"

    def __str__(self):
        return f"姓名:{self.__name}, 年龄:{self.age}, 学号:{self.id}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        return False


def add_stu(stu_list: list[Student]):
    name = input("请输入学生的姓名: ")
    age = int(input("请输入学生的年龄: "))
    id = int(input("请输入学生的学号: "))
    stu = Student(id, age, name)
    stu_list.append(stu)


def del_stu(stu_list: list[Student]):
    stu_id = int(input("请输入学生的学号: "))
    stu_list[:] = [stu for stu in stu_list if stu.id != stu_id]


def find_stu(stu_list: list[Student]):
    stu_id = int(input("请输入学生的学号: "))
    for stu in stu_list:
        if stu.id == stu_id:
            print(stu)
            break
    else:
        print(f"学号:{stu_id} 该学生不存在")


def update_stu(stulist: list[Student]):
    stu_id = int(input("请输入学生的学号: "))
    for stu in stulist:
        if stu.id == stu_id:
            print(stu)
            name = input("请输入学生的姓名: ")
            age = int(input("请输入学生的年龄: "))
            stu.age = age
            stu.name = name  # 直接修改私有属性
            break
    else:
        print(f"学号:{stu_id} 该学生不存在")


def print_stu(stu_list: list[Student]):
    for stu in stu_list:
        print(stu)


stu_list = list()
while True:
    number = int(input("输入1 添加学生 输入2 修改学生 输入3 删除学生 输入4 查询学生 输入5 打印所有学生 输入其他退出: "))
    if number == 1:
        add_stu(stu_list)
    elif number == 2:
        update_stu(stu_list)
    elif number == 3:
        del_stu(stu_list)
    elif number == 4:
        find_stu(stu_list)
    elif number == 5:
        print_stu(stu_list)
    else:
        break
```

