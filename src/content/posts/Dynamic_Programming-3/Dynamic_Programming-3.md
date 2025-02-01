---
title: 搞点Python778——day4
published: 2025-01-29
description: ''
image: 'dp3.jpg'
tags: [Study,Python,Dynamic_Programming]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

# 动态规划

## 背包DP

### 多重背包

- 多重背包也是0-1背包的一个变式。与 0-1 背包的区别在于每种物品是有限个，而非一个。分别用w、v、s代表体积、价值与数量。

- 状态定义：dp(i,j)：前i件物品，体积为j的最大价值

- 转换思路：

  1. （0-1背包）一种东西有k个，就可以当作k种状态，分别对应拿i个该东西，1<=i<=k，就把问题转换成一件的占用空间k\*vi ，价值为k\*wi的物品该不该拿。

     因此：状态转移方程为：

     ![](1.png)

  2. 优化上面的思路（0-1背包+完全背包）：对于有的物品，占用体积为 v，共有 s 件，存在s\*v >=V时，说明这个物品还没有拿完，背包就已经装不下了，等价于完全背包。完全背包时间复杂度相对要小一些。
  
    因此实现代码如下：
  
```python
import sys
input = lambda:sys.stdin.readline().strip()
N,V = map(int,input().split())
dp = [0] * (V+1)
for i in range(1,N+1):
    v,w,s= map(int,input().split())
    if v*s >= V:
        #完全背包
        for j in range(v,V+1):
            dp[j] = max(dp[j],dp[j-v]+w)
    else:
        #0-1背包
        for j in range(V,v-1,-1):
            for k in range(0,s+1):
                if j >= k*v:
                    dp[j] = max(dp[j],dp[j-k*v]+k*w)
print(dp[V])
```

- 优化方案

1. 二进制优化：优化拆分方式

   由01代码可以表示所有的数字，我们想到，用多个等比的2的次方数去表示所有的k。如果有无法消干净的情况，就在后面单独地补一个数。比方说：

   - 6 = 1 + 2 + 3

   - 8 = 1 + 2 + 4 + 1

   - 31 = 1 + 2 + 4 + 8 + 16

   可以知道，只要数字k不满足(k+1)是2的倍数，就要加上一个非2的倍数的数字。

   数字拆分之后，我们就把i一定的多个物品分成：1件价值为w体积为v的物品、1件价值为2w体积为2v的物品、一件价值为4w体积为4v的物品……最后还可能有系数不是2的指数的。

   按照这种方式拆分之后，再用这些物品表示所有的j的情况，用0-1背包的思路解决问题即可。
   
   代码实现如下：
   
```python

```
   

