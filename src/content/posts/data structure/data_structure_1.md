---
title: 搞点Python778——day11
published: 2025-07-17
description: 'Review data structures.'
image: '1.jpg'
tags: [Study,Python,Data Structure]
category: 'Python'
draft: false 
lang: 'zh_CN'
---
- [链表](#链表)
	- [分类](#分类)
	- [单链表](#单链表)
		- [数组模拟](#数组模拟)
		- [代码模板](#代码模板)
		- [例题：B3631 单向链表](#例题b3631-单向链表)
	- [双链表](#双链表)
		- [数组模拟](#数组模拟-1)
		- [代码模板](#代码模板-1)
		- [例题：B4324 【模板】双向链表](#例题b4324-模板双向链表)
	- [邻接表](#邻接表)
- [栈和队列](#栈和队列)
	- [区别](#区别)
	- [栈](#栈)
		- [数组模拟](#数组模拟-2)
		- [代码模板](#代码模板-2)
		- [例题：B3614 【模板】栈](#例题b3614-模板栈)
	- [队列](#队列)
		- [数组模拟](#数组模拟-3)
		- [代码模板](#代码模板-3)
		- [例题：B3616 【模板】队列](#例题b3616-模板队列)
- [单调栈和单调队列](#单调栈和单调队列)
	- [单调栈](#单调栈)
	- [例题模板：P5788 【模板】单调栈](#例题模板p5788-模板单调栈)
	- [单调队列](#单调队列)
	- [例题模板：P1886 滑动窗口 /【模板】单调队列](#例题模板p1886-滑动窗口-模板单调队列)
- [KMP](#kmp)
	- [预处理ne数组原理](#预处理ne数组原理)
	- [字串匹配原理](#字串匹配原理)
	- [例题：P3375 【模板】KMP](#例题p3375-模板kmp)

这个暑假也是好好开始刷算法题了，跟着acwing的课程先学数据结构！顺便也是把stl学了，做好ALL的准备👀

# 链表

## 分类

- 单链表：邻接表，用于存储树和图
- 双链表：用于优化某些题目

## 单链表

### 数组模拟

要包含两个方面的东西，用下标来关联：

1. value:e[N]（值）
2. next:ne[N]（下标）

![alt text](image.png)

### 代码模板

```python
# head
# e:value
# ne:next
# idx:当前用到的地址

# 初始化
def init():
    head = -1
    idx = 0 # 可以从0开始分配

# x值插入头节点
def add_to_head(x):
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1

# 将x值插入下标为k的值的后面
def add(x,k):
    e[x] = idx
    ne[x] = ne[k]
    ne[k] = idx
    idx += 1

# 将k下标之后的一个点删掉
# 有一点容易写错
def remove(k):
    ne[k] = ne[ne[k+1]]
```

### 例题：[B3631 单向链表](https://www.luogu.com.cn/problem/B3631)

但是这道题的实现跟acwing讲的还是不一样。题干的要求是在对应的元素后面添加、查询、删除数字，如果用acwing的做法还需要去遍历找到那个位置。这里的优化是直接用下标代替数值，只需要一个ne数组就可以实现。

```python
# 改进：用下表代替数值，直接在O(1)时间内完成
import sys
input = lambda:sys.stdin.readline()
N = 10**6+1
ne = [-1] * N
head = 1
q = int(input())
for _ in range(q):
	ii = list(map(int,input().split()))
	if ii[0] == 1:
		ne[ii[2]] = ne[ii[1]]
		ne[ii[1]] = ii[2]
	elif ii[0] == 2:
		print(ne[ii[1]] if ne[ii[1]] != -1 else 0)
	else:
		ne[ii[1]] = ne[ne[ii[1]]]
```

洛谷上的一个pypy3满分解法是用字典，跟我用数值直接对应下标的原理是相同的。

还有直接用列表的函数的。用数组确实会快很多。

```python
n = int(input())

l = [1, 0]

for i in range(n):
    k = [int(x) for x in input().split()]
    if k[0] == 1:
        (x, y) = k[1:3]
        l.insert(l.index(x) + 1, y)
    elif k[0] == 2:
        print(l[l.index(k[1]) + 1])
    else:
        del(l[l.index(k[1]) + 1])
```

## 双链表

### 数组模拟

相比于单链表：一个指向前，一个指向后

1. value:e[N]（值）
2. left:l[N]（下标）
3. rigth:r[N]（下标）

同时，对于节点下标，0表示最左侧，1表示最右侧

### 代码模板

```python
# e:value
# l:left
# r:right
# idx:当前用到的地址
# 0表示最左侧，1表示最右侧

# 初始化
def init():
    r[0] = 1
    l[1] = 0
    idx = 2 # 0和1已经被占用了

# 在k节点的右边插入一个点
def add(k,x):
    e[idx] = x
    # 先处理新的点，r[k]最后才能改变
    l[idx] = k
    r[idx] = r[k]
    l[r[k]] = idx
    r[k] = idx

# 在k节点的左边插入一个点等价于在k左边节点的右边插入一个点
def add_left(k,x):
    add(l[k],x)

# 删除第k个点
def remove(k):
    r[l[k]] = r[k]
    l[r[k]] = l[k]
```

### 例题：[B4324 【模板】双向链表](https://www.luogu.com.cn/problem/B4324)

为了判断链表是否为空，在1和N前后都添加了0和N+1。看了几个基本上都是用的r[head] == n+1判断的，应该还不错！

```python
import sys
input = lambda:sys.stdin.readline()
n,m = map(int,input().split())
l = [(i-1) for i in range(n+2)]
r = [(i+1) for i in range(n+2)]
head = 0
for _ in range(m):
	od = list(map(int,input().split()))
	if od[0] == 1 and od[1] != od[2]:
		# 删除xs
		r[l[od[1]]] = r[od[1]]
		l[r[od[1]]] = l[od[1]]
		# 插入到y左边
		r[l[od[2]]] = od[1]
		l[od[1]] = l[od[2]]
		r[od[1]] = od[2]
		l[od[2]] = od[1]
	elif od[0] == 2 and od[1] != od[2]:
		# 删除x
		r[l[od[1]]] = r[od[1]]
		l[r[od[1]]] = l[od[1]]
		# 插入到y右边
		r[od[1]] = r[od[2]]
		l[r[od[2]]] = od[1]
		r[od[2]] = od[1]
		l[od[1]] = od[2]
	else:
		r[l[od[1]]] = r[od[1]]
		l[r[od[1]]] = l[od[1]]
if r[head] == n+1:
	print("Empty!")
	exit()
while r[head] != n+1:
	print(r[head],end = ' ')
	head = r[head]
```

## 邻接表

相当于开了n个单链表，后面图论具体学习

![alt text](image-1.png)

# 栈和队列

## 区别

1. 栈：先进后出
2. 队列：先进先出

## 栈

### 数组模拟

栈从下标为1开始加入。

1. value:stk[N]
2. 栈顶:tt

### 代码模板
```python
# value:stk[N]
# 栈顶

# 初始
tt = 0

# 插入
stk[++tt] = x

# 栈顶元素
stk[tt]

# 弹出
tt -= 1

# 判断栈是否为空
if tt > 0: not empty
else:empty
```

### 例题：[B3614 【模板】栈](https://www.luogu.com.cn/problem/B3614)

```python
import sys
input = lambda:sys.stdin.readline()
t = int(input())
for _ in range(t):
	n = int(input())
	stk = [0] * (n+1)
	tt = 0
	for i in range(n):
		od = list(input().split())
		if od[0] == "push":
			tt += 1
			stk[tt] = od[1]
		elif od[0] == "query":
			if tt > 0: print(stk[tt])
			else: print("Anguei!")
		elif od[0] == "pop":
			if tt > 0: tt -= 1
			else: print("Empty")
		else: print(tt)
```

## 队列

### 数组模拟

队列从下标为0开始加入。

1. value:q[N]
2. 头:hh
3. 尾:tt

### 代码模板

```python
# value:q[N]
# 头:hh
# 尾:tt

# 初始化
tt = -1
hh = 0

# 拆入元素
q[++tt] = x

# 弹出
hh += 1

# 判断是否为空
if hh <= tt： not empty
else:empty

# 取出队头或者队尾元素
q[hh]
q[tt]
```

### 例题：[B3616 【模板】队列](https://www.luogu.com.cn/problem/B3616)

注意区分清楚hh为队首，tt为队尾，在队尾加入，在队首输出

```python
import sys
input = lambda:sys.stdin.readline()
n = int(input())
q = [0] * n
hh = 0
tt = -1
for i in range(n):
	od = list(map(int,input().split()))
	if od[0] == 1:
		tt += 1
		q[tt] = od[1]
	elif od[0] == 2:
		if hh <= tt: hh += 1
		else: print("ERR_CANNOT_POP")
	elif od[0] == 3:
		if hh <= tt: print(q[hh])
		else: print("ERR_CANNOT_QUERY")
	else:
		print(tt-hh+1)
```

# 单调栈和单调队列

用的情况很少

## 单调栈

- 应用场景：求某一个节点，左边比它小的、最近的节点

**考虑**：如果有a<sub>3</sub> > a<sub>5</sub>，那么a<ub>i</sub>(i>=6)的答案一定不是a<sub>3</sub>

**一般化**：a<sub>x</sub> <= a<sub>y</sub> （x<=y），那么a<sub>x</sub>就可以删掉

**结果**：维护一个单调上升的栈

![alt text](image-2.png)

- stk[tt] > a[i]：栈点就可以删掉。直到找到stk[tt] < a[i]

## 例题模板：[P5788 【模板】单调栈](https://www.luogu.com.cn/problem/P5788)

不幸的是会MEL。好在现在所有题目都是1025MB。128MB真是疯

```python
import sys
input = lambda:sys.stdin.readline()
n = int(input())
a = [0] + list(map(int,input().split()))
N = 3*10**6
stk = [0] * (n+1)
tt = 0
ans = [0] * n
for i in range(n,0,-1):
	# 维护单调性
	while tt!=0 and a[stk[tt]]<= a[i]: tt-=1
	ans[i-1] = stk[tt]
	tt += 1
	stk[tt] = i
print(*ans)
```

## 单调队列

- 应用场景：求解**滑动窗口**中的最小值

**一般化**：存在a<sub>i</sub> > a<sub>i+1</sub>，就可以把a<sub>i</sub> 删掉，最终变成一个严格单调上升的队列。

![alt text](image-3.png)

因此最小值就是队列的头（q[hh]）。

同时,单调队列习惯上存储的是数组的下标,便于控制队首是否应该出队

## 例题模板：[P1886 滑动窗口 /【模板】单调队列](https://www.luogu.com.cn/problem/P1886)

```python
import sys
input = lambda:sys.stdin.readline()
n,k = map(int,input().split())
a = list(map(int,input().split()))
q = [0] * n # 最小值
hh = 0
tt = -1
for i in range(n):
	# 达到滑动窗口的大小
	# 队首移出处理，至多只能移出去一个
	if hh <= tt and i-k >= q[hh]: hh+=1
	while hh <= tt and a[q[tt]] >= a[i]: tt -= 1
	tt += 1
	q[tt] = i
	if i >= k-1: print(a[q[hh]],end = ' ')
print()
hh = 0
tt = -1
for i in range(n):
	if hh <= tt and i-k >= q[hh]: hh+=1
	while hh <= tt and a[q[tt]] <= a[i]: tt -= 1
	tt += 1
	q[tt] = i
	if i >= k-1: print(a[q[hh]],end = ' ')
```

# KMP

- 用途：字符串匹配：在一个主字符串中查找某个子字符串出现的**所有*位置

**思想**：预处理出来每一个点为终点的后缀与前缀相等的最大长度

也就是说：

```python
# next[i] = j
p[1,j] = p[i-j+1,i]
```

模拟匹配过程理解next[i]=j的含义：

![alt text](image-4.png)

如果在p[i]的位置发现不匹配，就可以把p[j]移动到p[i]的位置，前面理论上是不用检验一定可以匹配成功的。

重复上述操作，就可以找到所有字串存在的位置。

因此kmp分成两个**步骤**：

## 预处理ne数组原理

- ne[1] = 0
- 假设已知ne[i-1]，比较p[ne[i-1]+1]和p[i]:
- 如果p[ne[i-1]+1]==p[i]：ne[i] = ne[i-1]+1
- 如果p[ne[i-1]+1]!=p[i]: 就把ne[i-1]移动到i-1的位置上，i-1之前还是吻合的。继续比较p[ne[i-1]+1]==p[i]。一直到ne[i-1] = 0就停止，此时说明只有与第一个字符相等或不相等的可能。

用案例说明：

```python
p = "abababab"
```

下标从1开始。设定ne[1] = 0

对于ne[2]：比较p[ne[i-1]+1]和p[i]。ne[i-1] = 0，已经退出循环

p[ne[i-1]+1] = p[1] = 'a'，不相等，所以ne[2] = 0

对于ne[3]：比较p[ne[i-1]+1]和p[i]。ne[i-1] = 0，已经退出循环

p[ne[i-1]+1] = p[1] = 'a'，相等，所以ne[3] = ne[i-1]+1

对于ne[4]：比较p[ne[i-1]+1]和p[i]。p[ne[i-1]+1] = p[2] = 'b'，相等，所以ne[4] = ne[i-1]+1 = 2

以此类推。

![alt text](9d8afdf2214de12055ce776a977eeac.png)

在具体实现中，可以用i遍历子串，用j来代表ne[i-1]的数值，在本轮循环中，如果配对成功，则j先自增，再ne[i] = j，如果配对不成功，则j不用自增，ne[i] = j，并且j的数值可以直接用于ne的下一位的计算中。

## 字串匹配原理

与ne数组生成原理基本类似，基本思想是如果本位不能匹配，就把前一位上的数用ne[i-1]来替换，对应匹配上的数量会减少，但是能够保证前面所有的字符串是能够匹配上的。

设定i遍历大串，用j遍历小串，j达到最长时，匹配数量加一，并且j变值为ne[j]，尽可能利用前面已经匹配的信息

## 例题：[P3375 【模板】KMP](https://www.luogu.com.cn/problem/P3375)

这里只要是注意下标是否从0开始，确定边界和输出.

```python
import sys
input = lambda:sys.stdin.readline()
s1 = input().rstrip()
s2 = ' ' + input().rstrip()
le = len(s2)
ne = [0] * le
j = 0
# 预处理ne[1] = 0
for i in range(2,le):
	while j!= 0 and s2[j+1] != s2[i]: j = ne[j]
	if s2[j+1] == s2[i]: j += 1
	ne[i] = j
# 字串匹配
L = len(s1)
j = 0
for i in range(L):
	while j!= 0 and s2[j+1] != s1[i]: j = ne[j]
	if s1[i] == s2[j+1]: j += 1
	if j == le-1:
		print(i-le+3)
		j = ne[j]
print(*ne[1:])
```

第一节课圆满结束！