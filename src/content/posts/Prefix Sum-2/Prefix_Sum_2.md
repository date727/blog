---
title: 搞点Python778——day7
published: 2025-03-04
description: 'Learn the prefix sum algorithm'
image: '2.jpg'
tags: [Study,Python,Prefix Sum]
category: 'Python'
draft: false
lang: 'zh_CN'
---

# 前缀和算法！启动！

有一阵子荒废了，昨天发烧+感冒确实是遭老罪，除了浑身没力气，消化功能也变差了很多很多。明天早上还是要喝点粥过渡一下，不要不吃早饭了。

今天开始写博客之前用打算用Haroopad打开md文件，结果等了很久都没打开，莫名其妙的，又不想再下载其他软件了，以后都直接用vscode的插件。所以程序员的尽头就是vscode()。

## 二维前缀和

### 二维前缀和的定义

sum(x,y)：从下标(0,0)到(x, y)子矩阵内元素的和【默认从(0,0)开始】。例如：sum(2,3)图示：

![](1.png)

为什么图中有一部分是标记为蓝色呢？要注意回顾，之前一维前缀和我们代码中有一句：

```python
#前缀和列表,注意这里有个添加0的处理
s = list(chain([0],list(accumulate(ls))))
```

在二维中也是一样，我们的数值是从(1,1)开始有定义的，(x,0)与(0,x)都默认为0。

### 二维前缀和递推公式

之前一维的递推公式：

```python
sum[i] = sum[i-1] + num[i]
```

结合经验，我们考虑x、y两个维度上面都减一，发现有面积重叠的部分，如图所示：

![](2.png)

因此我们也得到了最终的递推结论：

```python
sum[x][y] = sum[x-1][y] + sum[x][y-1] + num[x][y] - sum[x-1][y-1]
```

### 子矩阵求法

在前缀和的基础之上的一个应用，就是“开始点”不是(0,0)的时候可以怎么做。我们依旧用图像来理解：

![](3.png)

类似地，用两块长条减去重叠的部分，得到的结果再与前缀和相减就行。注意图示是一种特殊情况（正好重叠部分只有(0,0)一个点）

我们可以得到公式：要求出(x1,y1)到(x2,y2)之间的数的和(x1 < x2 , y1 < y2):

```python
sum = sum[x2][y2] - (sum[x1][y2] + sum[x2][y1] - sum[x1][y1])
=sum[x2][y2] + sum[x1][y1] - sum[x1][y2] - sum[x2][y1]
```

### 例题：[P1387 最大正方形](https://www.luogu.com.cn/problem/P1387)

这道题tag居然有dp，但是稍微一想确实有点像，但是这个题目与传统的dp直接输出dp\[n\][m]也并不相同。没错，本人就是在这个死胡同上栽了跟头。

我们用dp\[i\][j]定义的是**每个位置为右下角的最大正方形的边长**。递推的本质是你要去拓展，如果你在(x,y)点想要拓展正方形的边长，那你就得要求，首先它本身是1，其次它的左上三个点的位置的dp足够长。如果它本身就是0，那么就不可能构成正方形。有以下状态转移方程：

```python
if num[i][j] == 1:
    dp[i][j] = min(dp[i−1][j],dp[i][j−1],dp[i−1][j−1])+1
else:
    dp[i][j] = 0
```

所以说前缀和其实也算是动态规划常用到的工具，学习的顺序还是反了啊（冒汗）。

以下是编程实现：

```python
import sys
input = lambda: sys.stdin.readline().rstrip()
#数列表是从0开始的，dp列表是从(1,1)开始的
n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0] * (m+1) for _ in range(n+1)]
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            dp[i+1][j+1] = 0
        else:
            dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
            ans = max(ans, dp[i+1][j+1])
print(ans)
```

在洛谷上发现一开始下标并没有设置好，结果全AC了，在题解里面也看到说这道题用搜索、二分、暴力都行。emmm仁者见仁智者见智吧。