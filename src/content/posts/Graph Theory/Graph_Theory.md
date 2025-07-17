---
title: 搞点Python778——day11
published: 2025-04-11
description: 'Study Graph Theory and Basic Data Structure'
image: '1.jpg'
tags: [Study,Python,Graph Theory,Data Structure]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

- [ST表](#st表)
  - [模板题](#模板题)
  - [思想](#思想)
    - [预处理手段](#预处理手段)
    - [状态转移方程](#状态转移方程)
  - [模板题求解](#模板题求解)
- [图上的BFS、DFS](#图上的bfsdfs)


其实今天已经是最后一天了，好像再做什么努力也已经对明天作用不大。但是这一段时间很难得地别的事情都没有，安安心心地学算法（虽然一整天打游戏的时间也很多bushi）。希望比赛之后能够接着学Java，然后真的开始刷力扣什么的。加油啊加油。

基础的概念就不学了。

# ST表

解决RMQ（区间最大最小值）问题，可重复贡献问题

例如：区间最值、区间按位和、区间按位或、区间gcd，满足**x op x == x**

## 模板题

给定n个数字，m次询问，每次询问回答区间[l,r]中的最值。

暴力O(mn)

## 思想

倍增，动态规划

### 预处理手段

ST表的核心是对**每一个下标i**，预处理**i到i+2^j-1**的区间。

### 状态转移方程

划分成两个区间，起点不同


根据一个例子来看：

- f(i,0)：j=0，原数组；
- f(i,1)：j=1，长度为2的子数组，可以由f(i,0)得到；
- f(i,2)：j=2，长度为4的子数组，可以由f(i,1)得到.

对于任意询问而言，转换：

我们取最大的k，使得2^k不超过区间长度。两个区间都可以不遗漏地查找[l,r]

## [模板题求解](https://www.lanqiao.cn/problems/1205/learning/?page=1&first_category_id=1&tag_relation=union&problem_id=1205)

```python

```

# 图上的BFS、DFS






