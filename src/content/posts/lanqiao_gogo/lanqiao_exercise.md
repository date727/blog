---
title: 蓝桥杯官网刷题记录
published: 2025-02-27
description: 'Record of Solving Algorithm Problem Sets'
image: 'lanqiao.jpg'
tags: [Study,Python]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

# 蓝桥杯要刷题啊啊啊啊啊！

不知道自己考试前能不能够学完了，确实荒废了太久了，寒假学算法的时候就觉得，共情初中的时候学不会的自己吧嗯。今天总感觉自己基本的写python的能力都没有了，结果一看真是的。因为是python算法选手，还是用蓝桥杯官网的练习比较好。

## 2025/2/27

- [摆玩具](https://www.lanqiao.cn/problems/5888/learning/?page=1&first_category_id=1&tags=%E6%9E%9A%E4%B8%BE,%E6%A8%A1%E6%8B%9F,%E5%89%8D%E7%BC%80%E5%92%8C,%E5%B7%AE%E5%88%86,%E4%BA%8C%E5%88%86,%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2,%E8%B4%AA%E5%BF%83,%E4%BD%8D%E8%BF%90%E7%AE%97,%E5%8F%8C%E6%8C%87%E9%92%88&tag_relation=union&sort=difficulty&asc=1)

我还是挑的简单的，一上来就怀疑自己没有思路。有了思路之后搓代码，有想法又忘记了怎么写，真的废物一个啊，还不练习你真的找死啊。

### tag

贪心，极差，分段

### 思路

从极差的计算方式联想到了**数轴**，数字可以对应数轴上的点，两点之**差**可以用两点之间的**距离**来呈现。所以如果分段要求为1（也就是不分段），那么就是最大最小两个点之间的距离。分成n段，也就是拿掉(n-1)（**注意是n-1**）个两点间线段，最终的结果就是【最大最小两个点之间的距离-（n-1）个小分段的长度】。

由于问的是最小值，那么就要求小分段尽可能大。我采用的是**优先级队列**。在逐一读取数字时，计算数字之间的“距离”并插入优先级队列。注意优先级队列get是从序号小的开始，所以存入的“距离”应当是非正数。为什么说是非正数呢？注意题干中有个案例说明：

> {2}∣{5,7,10,13}，极差和为 0+8=8。

所以要考虑把第一个数字分成一段的情况，存入0。

以下是代码实践：
```python
import os
import sys
import queue
input = lambda:sys.stdin.readline().strip()
n,k = map(int , input().split())
q = queue.PriorityQueue()
numlist = list(map(int , input().split()))
p = numlist[0]
sum = numlist[n-1] - numlist[0]
for i in numlist:
  x = p - i
  q.put((x,i))
  p = i
for i in range(0,k-1):
  x = q.get()
  sum += x[0]
print(sum)
```

因为我电脑上的Python是anaconda自带的，自己把IDLE删掉了，所以代码也是在官网上敲好的，缩进就没有那么美观。测试是通过了，但是敲代码的能力是心知肚明的。唉，继续努力吧。
