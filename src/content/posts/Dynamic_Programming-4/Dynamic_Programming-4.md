---
title: 搞点Python778——day5
published: 2025-02-07
description: 'Essentially solved the knapsack problem!'
image: 'dp4.jpg'
tags: [Study,Python,Dynamic Programming]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

[TOC]

# 动态规划

## 背包DP

### 混合背包

- 混合背包就是将前面三种的背包问题混合起来，不同的物品的个数不同：一次，多次，无数次。因此按照以下的思路分类讨论即可：

```python
遍历物品：
   if 01背包：01背包处理逻辑
   elif 完全背包：完全背包处理逻辑
   else: 多重背包处理逻辑
```
正好可以梳理一下三种背包问题的逻辑区别，都是针对一维数组：

1. 01背包：

   （1）状态转移：dp[j] = max(dp[j - w] + v, dp[j])，源自：dp(i,j)= max( dp(i,j - w) + v, dp(i,j) ）
   （2）从右到左更新：for j in range(V,v-1,-1)

2. 完全背包：

   （1）状态转移：dp[j] = max(dp[j - w] + v, dp[j])，源自：dp(i,j)=max( dp(i-1,j) , dp(i,j-w[i])+v[i] )

   （2）从左到右更新：for j in range(v,V+1)

3. 多重背包：本来可以根据s*v与V的大小转换成前面两种的，这里梳理一下单调队列优化

   （1）对于任意一种物品，V%v = d的结果作为基底，循环遍历d,d+v,d+2v…；
   （2）单调队列保持maxlen=s+1，每次遍历先将单调队列中的元素都加w；
   （3）将dp值与队列最小值比较，队列最小值更小就删掉，更大就让dp值插入到队伍后面。
   （4）dp值重新赋值为单调队列的最大值。
   
### 二维费用背包

- 题干：有 n 个任务需要完成，完成第 i 个任务需要花费 ti 分钟，产生 ci 元的开支。现在有 T 分钟时间，W 元钱来处理这些任务，求最多能完成多少任务。

- 分析：任务只有完成和不完成两种情况，很显然二维费用背包就是有多个01背包限制，要考虑多个方面，其实也更加贴近生活吧。结合之前dp[j]的含义，我们使用**二维数组**dp(i,j)，表示在时间为i，开支为j的情况下能够完成的任务总数。尝试写代码：

```python
import sys
input = lambda: sys.stdin.readline().strip()
N,T,W = map(int, input().split())
dp = [[0] * (W+1) for _ in range(T+1)]
for i in range(N):
    t,c = map(int, input().split())
    for j in range(T,t-1,-1):
        for k in range(W,c-1,-1):
            dp[j][k] = max(dp[j][k], dp[j-t][k-c]+1)
print(dp[T][W])
```

案例输入：

```python
#n个任务，T时间，W元钱
6 10 10
1 1
2 3 
3 2
2 5
5 2
4 3
```

案例输出：

```python
4
```

在洛谷上面跑了，除了有一个超时，答案都没问题。

### 分组背包

- 题意：有 n 件物品和一个大小为 m 的背包，第 i 个物品的价值为 wi，体积为 vi。同时，**每个物品属于一个组**，同组内最多只能选择一个物品。求背包能装载物品的最大总价值。

- 分析：把问题分成两个步骤：（1）这个组选不选；（2）这个组里面选谁。

- 在存储上的考量：第几组，第几个，对应了体积与价值两个元素，所以用一个**二维数组**存储第几组，第几个的**序号**，序号对应用一维数组存储的体积与价值。由于有组别之间的限制，所以要先存储完之后再进行最大值的计算。尝试写代码：

```python
import sys
input = lambda: sys.stdin.readline().strip()
m,n = map(int, input().split())
t = [[0] * 1001 for _ in range(101)]
W=[0] * (n+1)
V=[0] * (n+1)
num = [0] * 101
sum = 0
for i in range(1,n+1):
    V[i], W[i], x= map(int, input().split())
    sum = max(sum,x)
    num[x]+=1
    t[x][num[x]] = i
dp = [0] * (m+1)
#遍历每一组
for i in range(1,sum+1):
    #遍历体积
    for k in range(m,-1, -1):
        #遍历物品
        for j in range(1,num[i]+1):
            if k >=V[t[i][j]] :
                dp[k] = max(dp[k],dp[k-V[t[i][j]]]+W[t[i][j]])
print(dp[m])
```

案例输入：

```python
#背包体积，物品个数
45 3
10 10 1
10 5 1
50 400 2
```

案例输出：

```python
10
```

要注意的就是先遍历体积后遍历物品，要不然就无法做到同一组别限制的作用（遍历下一个物品的时候同一体积的dp值可能会改变，表示接收两个及以上的同组物品）。

### 有依赖的背包

突然之间就上强度了。题目是[洛谷：金明的预算方案](https://www.luogu.com.cn/problem/P1064)

- 题意：金明有 n 元钱，想要买 m 个物品，第 i 件物品的价格为 vi，重要度为 pi。有些物品是从属于某个主件物品的附件，要买这个物品，必须购买它的主件。每个主件可以有 0 个、1 个或 2 个附件。

目标是让所有购买的物品的 vi\*pi 之和最大。

- 分析：我们把主件与对应的附件看成一个组别的，那么问题就转换成了**分组背包**。根据附件的个数，这个组别的物品个数也发生改变：假设主件为a，附件为b\_。按照主件+附件分类：

   1. a：a
   2. ab：a，ab
   3. ab1b2：a，ab1，ab2，ab1b2

当然也有可能不选。按照附件个数，我们对组别中的物品进行分别计算即可。

我写的是先把所有的主件+附件情况计算出来，之后再进行循环计算。大部分的题解都是先保存各自的数值，之后再进行计算的。有时间我补一下第二种的代码。

我一开始理解错误的一点就是q非0时的含义，我以为是只有主件参与讨论，事实上就对应循环的次数，结果两种想法的案例输出是一样的。虽然我做的明显更加合逻辑吧，但是这种思路未必在比赛中就不会出现。希望能够给出好的案例吧。

```python
import sys
input = lambda: sys.stdin.readline().strip()
m,n = map(int, input().split())
t = [[0] * 5 for _ in range(61)]
v_l = [[0] * 5 for _ in range(61)]
num = [0] * 61
for i in range(1,n+1):
    v,p,q= map(int, input().split())
    if q==0:
        t[i][1] = v * p
        v_l[i][1] = v
        if num[i] == 0:
            num[i] = 1
        else:
            if num[i] == 4:
                t[i][3] += v * p
                v_l[i][3] += v
                t[i][4] += v * p
                v_l[i][4] += v
            t[i][2] += v * p
            v_l[i][2] += v
    else:
        #主件先出来的
        if i >= q:
            if t[q][2] == 0:
                t[q][2] = v * p + t[q][1]
                v_l[q][2] = v + v_l[q][1]
                num[q] = 2
            else:
                t[q][3] = v * p + t[q][1]
                v_l[q][3] = v + v_l[q][1]
                t[q][4] = v * p + t[q][2]
                v_l[q][4] = v + v_l[q][2]
                num[q] = 4
        #附件先出来的
        else:
            if t[q][2] == 0:
                t[q][2] = v * p
                v_l[q][2] = v
                num[q] = 2
            else:
                t[q][3] = v * p
                v_l[q][3] = v
                t[q][4] = v * p + t[q][2]
                v_l[q][4] = v + v_l[q][2]
                num[q] = 4
dp = [0] * (m+1)
#遍历每一组
for i in range(1,n+1):
    #遍历体积
    for k in range(m,-1, -1):
        #遍历物品
        for j in range(1,num[i]+1):
            if k >= v_l[i][j] :
                dp[k] = max(dp[k],dp[k-v_l[i][j]]+t[i][j])
print(dp[m])
```

案例输入：

```python
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
```

案例输出：

```python
2200
```

