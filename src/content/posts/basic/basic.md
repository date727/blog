---
title: 搞点Python778——day9
published: 2025-03-30
description: 'learning basic algorithms'
image: '1.jpg'
tags: [Study,Python,Basic algorithms]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

# 枚举

## 是什么？

- 逐个尝试所有可能的**值或组合**来解决问题
- 问题空间必须是**离散**的

## 具体步骤

1. 确定解空间：一维？二维？；
2. 确定空间边界：最值、步长；
3. 估算**时间复杂度**，优化。

## 例题：百钱买百鸡

![](1.png)

- 思路一：枚举三种鸡的数量

公鸡上限：100 // 5 = 20

母鸡上限：100 // 3 = 33

小鸡上限：100 * 3 = 300 > 100，可以限定上线为100

时间复杂度：20\*33\*100

- 思路二：枚举两个变量

假设枚举公鸡为x只，母鸡为y只

小鸡用的钱：(100 - 5x - 3y)

小鸡的数量：3(100 - 5x - 3y)

时间复杂度：20\*33

- 思路三：枚举一个变量，后面两个变量通过二元一次方程组求解

时间复杂度：20

## 例题：[字符计数](https://www.lanqiao.cn/problems/160/learning/?page=1&first_category_id=1&tag_relation=union&name=%E5%AD%97%E7%AC%A6%E8%AE%A1%E6%95%B0)

没有什么特别能说的，主要就是记得，判断字符是否在字符串中可以直接用if c in 字符串，不用把字符串转成列表。

## 例题：[反倍数](https://www.lanqiao.cn/problems/152/learning/?page=1&first_category_id=1&tag_relation=union&name=%E5%8F%8D%E5%80%8D%E6%95%B0)

记录一个课上的笔记：**容斥原理**

1. [1,n]中a的倍数个数：n // a;
2. [1,n]中b的倍数个数：n // b;
3. [1,n]中ab的倍数个数：n // ab;
4. [1,n]中a的倍数或者b的倍数个数：n // a + n // b - n // ab;

# 模拟

## 含义

直接按照题目含义模拟

## 注意事项

1. 读懂题目；
2. 步骤与代码一一对应；
3. 提取重复部分，写成对应函数；
4. 分块调试。

## 例题：[饮料换购](https://www.lanqiao.cn/problems/143/learning/?page=1&first_category_id=1&tags=%E6%9E%9A%E4%B8%BE,%E6%A8%A1%E6%8B%9F,%E5%89%8D%E7%BC%80%E5%92%8C,%E5%B7%AE%E5%88%86,%E4%BA%8C%E5%88%86,%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2,%E8%B4%AA%E5%BF%83,%E4%BD%8D%E8%BF%90%E7%AE%97,%E5%8F%8C%E6%8C%87%E9%92%88&tag_relation=union&name=%E9%A5%AE%E6%96%99%E6%8D%A2%E8%B4%AD)

编程实现：

```python
import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
sum = n
f = 0
while n != 0:
    f+=1
    n-=1
    if f==3:
        f=0
        n+=1
        sum+=1
print(sum)
```

老师讲的减少循环的方法：

```python
#n：瓶盖数
#ans：饮料
n = int(input())
ans = n 
while True:
    if n>=3:
        #把三个瓶盖换成一瓶饮料
        n-=3
        #统计饮料
        ans += 1
        #更新瓶盖
        n += 1
    else:
        break
print(ans)
```

优化：

```python
#n：瓶盖数
#ans：饮料
n = int(input())
ans = n 
while True:
    if n>=3:
        #n个瓶盖可以换n//3个饮料，剩余n%3
        #统计饮料
        ans += n // 3
        #更新瓶盖
        n = n%3 + n//3
    else:
        break
print(ans)
```

## 例题：[图像模糊](https://www.lanqiao.cn/problems/550/learning/?page=1&first_category_id=1&tags=%E6%9E%9A%E4%B8%BE,%E6%A8%A1%E6%8B%9F,%E5%89%8D%E7%BC%80%E5%92%8C,%E5%B7%AE%E5%88%86,%E4%BA%8C%E5%88%86,%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2,%E8%B4%AA%E5%BF%83,%E4%BD%8D%E8%BF%90%E7%AE%97,%E5%8F%8C%E6%8C%87%E9%92%88&tag_relation=union&name=%E5%9B%BE%E5%83%8F)

可以用之前扫雷一样的，用dir记录偏移值。也可以用一个双重循环，跟遍历dir的循环次数是一样的。

一个比较不好的习惯就是变量重复定义，导致很难找的错误。

编程实现：

```python
import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int , input().split())
num = []
for i in range(n):
    ls = list(map(int , input().split()))
    num.append(ls)
    #ls为二维数组
ans = [[0] * m for _ in range(n)]
#dir = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
for i in range(n):
    for j in range(m):
        sum = 0
        count = 0
        #遍历每个位置求结果
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                #和dir一样的效果
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m:
                    sum+=num[x][y]
                    count += 1
        ans[i][j] = sum // count
for a in ans:
    print(" ".join(map(str,a)))
```

## 例题：[螺旋矩阵]()

### 模拟行进过程

```python
# 第一步
x,y=0,0
value = 1
num[x][y] = value
while value < n * m:
    #不断向右走，保证下一个点不越界、没数字
    while y+1 < m and num[x][y+1] == 0:
        value += 1
        y += 1
        num[x][y] = value
    #不断向下走，保证下一个点不越界、没数字
    while x+1 < n and num[x+1][y] == 0:
        value += 1
        x += 1
        num[x][y] = value
    #不断向左走，保证下一个点不越界、没数字
    while y - 1 >= 0  and num[x][y-1] == 0:
        value += 1
        y -= 1
        num[x][y] = value
    #不断向上走，保证下一个点不越界、没数字
    while x - 1 >= 0  and num[x-1][y] == 0:
        value += 1
        x -= 1
        num[x][y] = value
```

### 拓展：横折的方式

```
1 2 6 7 
3 5 8 13 
4 9 12 14
10 11 15 16

```

# 递归

## 是什么？

通过自己调用自己来解决问题的函数。通常把**大型复杂**问题层层转化为一个**与原问题相似的、规模较小**的问题求解。

## 注意事项

1. 递归出口
2. 如何化成子问题

同时可以作为函数的书写顺序。

