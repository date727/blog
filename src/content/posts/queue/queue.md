---
title: Python中的数据结构——队列与栈
published: 2025-02-06
description: 'Queues in Python'
image: 'queue.jpg'
tags: [Study,Python,queue]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

# queue模块

从多重背包单调队列过来补的。所以说学习是个系统的活，像本人这种乱投胎的行为只会变得很混乱。好在现在有时间可以好好学习。学习资源有：

1. [详解](https://blog.csdn.net/qq_52007481/article/details/125673224)

2. [Queue用法](https://blog.csdn.net/weixin_43533825/article/details/89155648)

## 为什么需要队列？

> 队列在[多线程编程](https://so.csdn.net/so/search?q=多线程编程&spm=1001.2101.3001.7020)中非常有用，因为它们允许线程之间安全地共享数据。

> 在python中，多个线程之间的数据是共享的，多个线程进行数据交换的时候，不能够保证数据的安全性和一致性，所以当多个线程需要进行数据交换的时候，队列就出现了，队列可以完美解决线程间的数据交换，保证线程间数据的安全性和一致性。

CUDA略微讲过线程，但是在Python中我也没用过，就放在这里吧。菜鸟教程里面也用列表去处理队列的问题，之后也学学吧。

## 类型

1. Queue：先进先出(FIFO)，一般我们就是说这个。
2. LifoQueue：后进先出(LIFO)，也就是**栈**（也就是queue模块其实包含了很多内容）
3. PriorityQueue：优先级队列（哎呦我操可算把你盼来了）

## 具体使用

### 导入模块

```python
import queue
```

### 创建队列

这里我感觉写全名没有任何问题，毕竟在比赛的时候没有办法用tab键补全。

```python
fifo_queue = queue.Queue()
lifo_queue = queue.LifoQueue()
priority_queue = queue.PriorityQueue()
```

用maxsize限制元素最多的个数，maxsize为0或者负数时表示无上限，没限制默认maxsize=0。

### 常用方法

假设q是队列。

| 方法        | 功能                                            |
| ----------- | ----------------------------------------------- |
| q.qsize()   | 获取队列的大小                                  |
| q.empty()   | 判断队列是否为空，返回True/False                |
| q.full()    | 判断队列是否放满了，对应maxsize。返回True/False |
| q.put(item) | 向队列存放数据                                  |
| q.get()     | 从队列获取数据                                  |

1. q.put(item)

   一般都是存放数据，直接用q.put(n)就行。对于优先级队列，数值与次序的存放，插入的格式变成了：

   ```python
   q.put((priority number, data))
   ```

   priority number越小，优先级越高。这里写一个案例与后面的get一起使用：

```python
#put()
for i in range(5):
    fifo_queue.put(i)
    lifo_queue.put(i)
priority_queue.put((1,'java'))
priority_queue.put((2,'golang'))
priority_queue.put((0,'python'))
priority_queue.put((0,'c++'))
```

2. q.get()

   主要就是get输出的顺序。优先级越高越先输出。对于优先级队列，优先级一样，数据部分可以比较大小。使用前面的案例编程：
   
```python
print(fifo_queue.get())
print(lifo_queue.get())
print(priority_queue.get())
```

得到输出：

```python
0
4
(0, 'c++')
```

可见优先级队列并没有按照输入的顺序输出的，而是按照优先级顺序输出的。

3. 其他关于数值的方法使用：

承接上会：fifo_queue与lifo_queue中应该分别有4个元素，优先级队列中有2个。编程如下：
```python
print(f"fifo_queue:qsize:{fifo_queue.qsize()},full?:{fifo_queue.full()},empty?:{fifo_queue.empty()}")
print(f"lifo_queue:qsize:{lifo_queue.qsize()},full?:{lifo_queue.full()},empty?:{lifo_queue.empty()}")
print(f"priority_queue:qsize:{priority_queue.qsize()},full?:{priority_queue.full()},empty?:{priority_queue.empty()}")
```

得到结果：因为没有限制maxsize，所以full()永远返回False。

```python
fifo_queue:qsize:4,full?:False,empty?:False
lifo_queue:qsize:4,full?:False,empty?:False
priority_queue:qsize:3,full?:False,empty?:False
```

# deque模块

deque模块是python标准库**collections**中的一项，它提供了**两端都可以操作**的序列。之后也要系统学一下collections。一个我觉得写collections的很完整的[链接](https://zhuanlan.zhihu.com/p/343747724)，然后[这个](https://blog.csdn.net/chl183/article/details/106958004)写queue也不错。

## 具体使用

### 创建deque序列

```python
from collctions import deque
d = deque()
```

初始化可以用maxlen限制元素个数。当限制长度的deque增加超过限制数的项时，**另一边的项**会自动删除。同时，deque 构造函数会将可迭代对象（列表、元组、字典、字符串等）作为输入。以下是一些可能会用得到的情况：

```python
d1 = deque("hello")
d2 = deque(range(10))
d3 = deque(["hello", "world"])
print(d1)
print(d2)
print(d3)
```

得到输出：

```python
deque(['h', 'e', 'l', 'l', 'o'])
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
deque(['hello', 'world'])
```

### 具体使用

1. 支持用下标访问元素：例如对之前的d1使用：

```python
print(d1[1])
```

可以得到输出：

```python
e
```

2. 一些方法使用：跟列表很像，非常好。

| 方法                   | 功能                                                         |
| ---------------------- | ------------------------------------------------------------ |
| d.append(item)         | 从右边添加某个元素                                           |
| d.appendleft(item)     | 从左边添加某个元素                                           |
| d.extend()             | 从右端逐个添加可迭代对象                                     |
| d.extendleft()         | 从左端逐个添加可迭代对象                                     |
| d.pop()                | 移除列表最右端的元素，并且返回该元素的值，如果没有元素将会报出IndexError |
| d.popleft()            | 移除列表最左端的元素，并且返回该元素的值，如果没有元素将会报出IndexError |
| d.count(item)          | 统计队列中的元素个数                                         |
| d.insert(index,object) | 在指定位置插入元素                                           |
| d.rotate(n)            | 顺时针旋转n步，d.rotate(1)相当于d.appendleft(d.pop())        |
| d.reverse()            | 逆序        |
| d.remove(item)         | 移除第一次出现的元素，如果没有找到，报出ValueError           |
| d.clear()              | 将deque中的元素全部删除                                      |
| d.copy()              | 返回一个一模一样的                                    |

编程练手：

```python
d.append(1)
d.extend([2,3,4])
d.appendleft(4)
d.extendleft([1,2,3])
print(d)
print(d.pop())
print(d.popleft())
print(d)
print(d.count(2))
d.remove(2)
print(d)
d.rotate(3)
print(d)
d.reverse()
print(d)
d.clear()
print(d)
```

得到输出：

```python
#注意extendleft是一个一个往左边放的
deque([3, 2, 1, 4, 1, 2, 3, 4])
4
3
#pop完后的结果
deque([2, 1, 4, 1, 2, 3])
2
#删去从左往右第一个2
deque([1, 4, 1, 2, 3])
#顺时针三次
deque([1, 2, 3, 1, 4])
#逆序之后
deque([4, 1, 3, 2, 1])
#清空之后
deque([])
```

注意，不能用d.pop()==IndexError去判断队列是否为空。可以直接用**while d**。
