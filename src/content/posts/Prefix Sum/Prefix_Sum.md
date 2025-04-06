---
title: 搞点Python778——day6
published: 2025-02-28
description: 'Learn the prefix sum algorithm'
image: 'Prefix Sum.jpg'
tags: [Study,Python,Prefix Sum]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

# 前缀和算法！启动！

前缀和在我上学期刷蓝桥杯模拟的时候看到过，没有深入去了解算法，自己从字面上猜了一下，觉得思路很通畅。这一次系统地学习一下。

参考的博客：

1.[超详细讲解前缀和](https://blog.csdn.net/qq_45914558/article/details/107385862)

2.[oi.wiki](https://oi-wiki.org/basic/prefix-sum/)

3.[迭代器](https://blog.csdn.net/xcntime/article/details/115675908)

## 一维前缀和

### 前缀和定义

前缀和就是从**位置1**到**位置i**这个区间内的所有的数字之和，是原始数组的元素依次累加的结果，用于高效地计算数组中某个范围内元素的和。

类似地可以定义前缀积与前缀异或和，但是应用并没有看到。

### 题目引入

- 输入一个长度为n的**整数序列**。接下来再输入m个**询问**，每个询问输入一对l, r。对于每个询问，输出原序列中从第l个数到第r个数的和。

- 输入格式
  第一行包含两个整数n和m。

  第二行包含n个整数，表示整数数列。

  接下来m行，每行包含两个整数l和r，表示一个询问的区间范围。

- 输出格式
  共m行，每行输出一个询问的结果。

- 数据范围
  1≤l≤r≤n,
  1≤n,m≤100000,
  −1000≤数列中元素的值≤1000
- 输入样例：
  
  ```python
  5 3
  2 1 3 6 4
  1 2
  1 3
  2 4
  ```
- 输出样例：
  
  ```python
  3
  6
  10
  ```

这就是一个非常典型的前缀和案例。设想一下如果我们用传统方式，代码的关键步骤：

```python
sum = 0
for i in range(l,r+1):
	sum += ls[i]
print(sum)
```

除了这个循环，我们还需要对于m个询问进行循环。在计算过程中，我们就会发现，进行了很多次重复的计算，比如询问[2,5]与[3,7]，中间[3,5]的部分我们是多次计算的。

因此我们就使用到前缀和的技术！对于数列表n，我们可以用列表s[i]记录n[0]~n[i]的所有数的和。显然：

```python
if i == 0:
    a[i] = n[i]
else:
    a[i] = n[i] - n[i-1]
```

这跟高中学的数列也很像了。要从n列表计算s列表的话，我们可以用一下的代码：

```python
s[0] = n[0] 
for i in range(1,num+1):
	s[i] = s[i-1] + n[i]
```

对于询问[l,r]，我们可以用**s[r] - s[l-1]**一步到位计算，相比于之前的思路时间复杂度就降低了很多。

感谢oi.wiki！让我看到了Python的宝藏库——itertools！

### 迭代器itertools

首先我们了解一下什么是**惰性**

- 惰性：不主动去遍历它，就不会计算其中元素的值；
- 惰性计算：包括延迟计算与短路求值。目的是要最小化计算机要做的工作；
- 惰性序列：表达式和变量绑定后不会立即进行求值，而是当你用到其中某些元素的时候才去求某元素对的值。

在Python中，**迭代器**是常用来做惰性序列的对象。由于惰性，迭代器可以用来存储**无限大的序列**。

迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。可以被循环遍历的对象被称为可迭代对象，包括range()、列表对象等。

常用到的是使用列表构造迭代器，我们可以用iter()函数将列表转换为迭代器。例如：

```python
ls = [1,2,3,4,5]
it = iter(ls)  #创建迭代器对象
```

而列表与迭代器的主要区别在于：

- 列表不论遍历多少次，表头位置始终是第一个元素；
- 迭代器遍历结束后，不再指向原来的表头位置，而是为**最后元素的下一个位置**；

我们由编程验证：
```python
for i in ls:
    print(i,end=' ')
print()
for i in ls:
    print(i,end=' ')
print()
for i in it:
    print(i,end=' ')
print()
for i in it:
    print(i,end=' ')
print()
```

会得到输出：
```python
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 

```

第二次遍历it不会有任何结果，因为第一次遍历已经到了末尾。

Python的内置模块itertools就是用来操作迭代器的一个模块，其中函数主要分成以下三类：无限迭代器，有限迭代器，组合迭代器。

**无限迭代器**：

用到的函数：

| 函数                    | 功能                                                         |
| ----------------------- | ------------------------------------------------------------ |
| count(start,step)       | 创建一个迭代对象，生成从start开始的连续整数，步长为step      |
| cycle(iterable)         | 创建一个迭代对象，对于输入的iterable的元素反复执行循环操作   |
| repeat(object[, times]) | 创建一个迭代对象，重复生成object，次数为times，如果没有设置times，则会无线生成对象 |

编程效果如下：
```python
from itertools import *
for i in count(2,4):
    if i == 18:
        break
    print(i,end=' ')
print()
f = 0
for i in cycle([1,2,3]):
    f += 1
    print(f"{i}:{f}")
    if f==3:
        break
for i in repeat("passion!",3):
    print(i)
```

输出结果如下：

```python
2 6 10 14 
1:1
2:2
3:3
passion!
passion!
passion!
```

**有限迭代器**/**输入序列迭代器**

函数如下：

|函数|功能|
|--------|--------|
|accumulate(iterable [,func])|创建一个迭代对象，由特定的二元函数的累计结果生成，默认进行进行累加操作（就是我们需要的前缀和）|
|chain(*iterables)|创建一个迭代对象，多个可迭代对象组合起来，形成一个更大的迭代器。|

先学到这里吧，感觉就这几个能用上。

iterable与\*iterables的区别在于iterable是可迭代对象，如列表、range()等；而\*iterables是多个可迭代对象。【个人感觉，也不是很准确】

编程感受：

```python
#前缀和
for i in accumulate(range(1,5)):
    print(i,end= ' ')
print()
#前几项中最大的数字
for i in accumulate([2,1,3,8,4,6],max):
    print(i,end = ' ')
print()
#将两个可迭代对象组合起来
for i in chain([1,4],"dsfe"):
    print(i,end=' ')
```

得到输出如下：

```python
1 3 6 10 
2 2 3 8 8 8 
1 4 d s f e 
```

**组合迭代器**

函数如下：

|函数|功能|
|--------|--------|
|product(*iterables, repeat=1)|创建一个迭代对象，返回多个可迭代对象的**笛卡儿积**，repeat 参数表示这些可迭代序列重复的次数）|
|permutations(iterable,r)|创建一个迭代对象，以元组形式返回可迭代对象中元素的**排列**。r默认为None，表示的是返回元组的长度|
|combinations(iterable,r)|创建一个迭代对象，以元组形式返回可迭代对象中元素的**组合**。r默认为None，表示的是返回元组的长度|
|combinations_with_replacement(iterable, r)|创建一个迭代对象，以元组形式返回可迭代对象中可与自身重复的元素的**组合**。r默认为None，表示的是返回元组的长度|

编程感受：

```python
for i in product([1,2],[3,4]):
    print(i, end=' ')
print()
for i in permutations([1,2,3],2):
    print(i,end=' ')
print()
for i in combinations([1,2,3],2):
    print(i,end=' ')
print()
for i in combinations_with_replacement([1,2,3],2):
    print(i,end=' ')
```

得到输出：

```python
(1, 3) (1, 4) (2, 3) (2, 4) 
(1, 2) (1, 3) (2, 1) (2, 3) (3, 1) (3, 2) 
(1, 2) (1, 3) (2, 3) 
(1, 1) (1, 2) (1, 3) (2, 2) (2, 3) (3, 3) 
```

### 使用accumulate完成习题

编程实现：

```python
from itertools import *
import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
#数列表
ls = list(map(int,input().split()))
#前缀和列表,注意这里有个添加0的处理
s = list(chain([0],list(accumulate(ls))))
for i in range(m):
    l,r = map(int,input().split())
    print(f"{s[r] - s[l-1]}")
```

ok因为有一个新的模块，这篇博客就到这里吧！下一次就上二维的！