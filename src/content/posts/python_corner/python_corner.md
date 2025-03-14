---
title: Python妙蛙
published: 2025-01-24
description: 'Some unsystematic Python knowledge in certain corners'
image: 'corner.jpg'
tags: [Study,Python]
category: 'Python'
draft: false
lang: 'zh_CN'
---
# 一些偶遇的知识
开此帖记录一些学习过程中遇到的很妙的技巧！
## print(f"")
以前学python一直用的就是print("…{}…".format(…))，在datawhale的AI Agent学习过程中第一次见到这个新的用法。在**Python3.6**（蓝桥杯可以用）之后，引入了f字符串（formatted string literals），一种更方便的**格式化字符串**输出方式。
引号使用单引号和双引号都可以。

1. 使用特点：在字符串中（'{}'内'）嵌入**表达式**，这些表达式在运行时会被其值所替换.
2. 用法：

- 变量

编写代码如下：

```python
name = "Ryuhana"
print(f"Hello, {name}!") 
```

得到输出：

```python
Hello, Ryuhana!
```

- 表达式求值

编写代码如下：

```python
a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}")
```

得到输出：

```python
The sum of 10 and 20 is 30
```

- 数据结构

以列表为例

```python
list=[1,2,3,4,5]
print(f"{list[1]}+{list[2]}={list[1]+list[2]}")
```

得到输出：

```python
2+3=5
```

- 函数调用

编写代码如下：

```python
def max(a,b):
    if a>b:
        return a
    else:
        return b
        
print(f"The bigger num between {a} and {b} is {max(a,b)}")
```

得到输出如下：

```python
The bigger num between 10 and 20 is 20
```

- 格式化输出
与format中的格式化方式是一样的，例如：

**浮点数保留小数点**(基本上也只会考到这个)

编写代码如下：

```python
r = 2
pi = 3.1415926
print(f"The area of the circle is: {pi*r*r:.2f}")
```

得到输出：

```
The area of the circle is: 12.57
```

**指定字段宽度和对齐**

很喜欢的例子：

```python
print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")
```

输出：

```
Left       |   Center   |      Right
```

## map()：一个可以替代循环的函数
Python的一个内置函数，能够根据提供的**函数**对指定的序列做映射。

1. 语法格式：map(function, iterable, ...)
> iterable：一个或多个**序列**

2. 返回值：返回包含每次 function 函数**返回值**的**迭代器**（还需要用list做进一步转化）。
3. 原理细化：

- 函数有一个形参

第一个参数 function 以参数序列中的每一个元素调用 function 函数。比如：

```python
def func(x):
    return 3*x
print(list(map(func,[1,2,3,4,5])))
```

输出：

```
[3, 6, 9, 12, 15]
```

- 函数有多个形参

多个列表，对应位置的列表数据进行相加。空缺的位置用**None**填补，可能会报错。例如：

```python
print(list(map(lambda x,y: x*y, [1, 2, 3, 4, 5],[1, 2, 3, 4, 5])))
```
执行效果是1，2，3，4，5的平方：

```
[1, 4, 9, 16, 25]
```

# 字符串函数

## 变换大小写

| 函数    | 功能       |
| ------- | ---------- |
| title() | 首字母大写 |
| upper() | 全部大写   |
| lower() | 全部小写   |

编程实践：

```
s = "Hello world"
print(s.title())
print(s.upper())
print(s.lower())
```

得到输出：

```
Hello World
HELLO WORLD
hello world
```

## 删除空白

| 函数     | 功能           |
| -------- | -------------- |
| strip()  | 删除两端的空白 |
| lstrip() | 删除左边的空白 |
| rstrip() | 删除右边的空白 |

都不会改变字符串原本的内容。

编程实践：

```python
s = " Hello world "
print(f"_{s.strip()}_")
print(f"_{s.lstrip()}_")
print(f"_{s.rstrip()}_")
```

得到输出：

```python
_Hello world_
_Hello world _
_ Hello world_
```

# 集合

确实这方面没怎么学好。

1. 无序性、不重复性
2. 大括号声明集合，例如：

```python
a = {1,2,3}
b = {2,4,3}
```

3. 支持交、并、差、环合运算：环合就是两个差集的和

```python
print(a|b) # 并集
print(a&b) # 交集
print(a-b) # 差集
print(a^b) # 环合
```

得到输出：

```python
{1, 2, 3, 4}
{2, 3}
{1}
{1, 4}
```

4. 字符串转化为集合

使用**set()**函数。例如：

```python
s = "Hello world"
print(set(s))
```

得到输出：

```python
{'o', 'r', 'e', 'l', 'd', ' ', 'w', 'H'}
```