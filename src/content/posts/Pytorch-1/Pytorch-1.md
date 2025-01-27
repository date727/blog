---
title: 学习深度学习——Numpy基础
published: 2025-01-27
description: 'Study Numpy Basic Syntax'
image: 'Pytorch_1.jpg'
tags: [Study,Python,Deep Learning]
category: 'Deep Learning'
draft: false 
lang: 'zh_CN'
---

# 学习深度学习

深度学习是大创要用到的东西，之前是看吴恩达大佬的课，后来闲置了就忘了一大堆。骐骥团队的AI组也是要系统学习深度学习（这句话说的好怪啊hhh），趁这个机会补回来吧。

一些资料：
1. [lab任务](https://github.com/deeplearningzerotoall/PyTorch.git)
2. [Pytorch手册](https://github.com/zergtant/pytorch-handbook/)

# 手册第一章

## 1.1 Pytorch简介

### Pytorch与Torch

1. 相同的底层：所有相同性能的C库：TH， THC， THNN， THCUNN，并且它们将继续共享这些库。
2. 上层包装语言不同：Pytorch是Python，Torch是lua

### 介绍一下

- 基于Torch的Python开源机器学习库，用于自然语言处理等应用程序
- 由Facebook的人工智能研究小组开发。
与Google的Tensorflow一起，是最火的两个深度学习框架。

- 作为一个Python包，提供两个高级功能：

1. 具有强大的GPU加速的张量计算（如NumPy）
2. 包含自动求导系统的的**深度神经网络**

### 对比PyTorch和Tensorflow

>PyTorch更有利于研究人员、爱好者、小规模项目等快速搞出原型。而TensorFlow更适合大规模部署，特别是需要跨平台和嵌入式部署时。

[整篇文章](https://zhuanlan.zhihu.com/p/28636490)就看懂了这个（）埋个坑在这里吧，希望之后能够看懂。

## 1.2 Pytorch环境搭建

> 有时候环境搭建困难的原因就是根本没人说搭建环境是在干什么

用轻薄本的有福了，本人就是只能下载CPU版本的Pytorch（）。

感觉那本手册里面讲的不清楚，也没讲anaconda的下载，所以放几个链接在这里：

1. [Pytorch的下载](https://blog.csdn.net/qq_43596278/article/details/136305903)（看到作者用的也是HP战66，很痛苦啊兄弟们，为什么当初不多花点钱上个独立显卡）

在看这篇博客之前，我下载的时候有遇到过启动不了的情况，查询了发现是下载前没有**安装虚拟环境**。后来安装了虚拟环境又因为Python的版本问题下载了很多遍（所以下载之前最好查一下Python下载哪个版本比较好，印象中版本太新的版本可能深度学习用不了），所以重复的工作做了很多次。至于为什么要安装虚拟环境，网上给出的答案：

- 避免依赖冲突：项目对于Pytorch的版本需求可能是不一样的，据说有的2.x无法兼容1.x的部分功能。
- 保护系统环境：如果在全局环境中随意安装各种版本的 PyTorch 和其他库，可能会破坏系统环境的稳定性
- **方便配置和迁移**：在开发项目时，通常需要记录项目所依赖的库及其版本号等信息。虚拟环境可以将这些依赖信息集中管理，通过生成**requirements.txt**等文件，可以方便地在不同的开发环境或服务器上重新创建相同的环境，实现项目的快速迁移和部署。这就可以方便团队开发。

*年轻的时候觉得配置环境是很有意思的事情，老了就开始觉得这太麻烦了。*

放点我能用得上的命令吧：

- **创建虚拟环境**：

  ```
  conda create -n <虚拟环境名字> python=<版本>
  ```

- **删除虚拟环境**：

  ```
  conda remove -n <虚拟环境名字> --all
  ```

- **启动虚拟环境**：

  ```
  conda activate pytorch
  ```

  我在虚拟环境配置好之前其实已经可以运行lab中的代码，因为配置这个环境我间断了很长时间（这不是一个好习惯），所以原因我也不清楚，可能是当初第一次用Jupyter Notebook发现运行不了就直接在这个环境中下了python编译器，跟一开始稀里糊涂地用pycharm一样。

2. 配置 Jupyter Notebook：配置前肯定是要下载的（）我也不记得是不是下载Anaconda的时候会顺便下好了，反正发现电脑中没有这个东西就下载一下就好。原手册开头还是蛮好的，但是你可能发现：
   - .py文件里根本没配置那两个语句，直接自己写就行；
   - 修改完之后可能打开还是C盘的路径，这是因为工作没做完，续上[Jupyter Notebook配置指导](https://blog.csdn.net/weixin_45640009/article/details/122082263)应该就能实现。（发现手册中间其实也有，但是起始位置那一栏没有改，本人也不知道改不改会不会有什么影响。只能说环境配置确实是因人而异的活）

## 1.3 60分钟(不是哥们)快速入门 （官方）

有点神魔这个标题SOS。因为不是很习惯中文翻译的学习方式所以还是去[官网](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)学习了一下。

### 张量（Tensors）

张量是一种特殊的**数据结构**，与数组和矩阵非常相似。

张量类似于NumPy的ndarray（**N维数组对象**），不同之处在于张量可以在 GPU 或其他专用硬件来加速计算。

我感觉手册和lab都有点突如其来（）所以看了[菜鸟教程](https://www.runoob.com/numpy/numpy-ndarray-object.html)。

**NumPy Ndarray 对象**

```python
import numpy as np
```

- 用于存放同类型元素的多维数组，每个元素在内存中都有相同存储大小的区域

- 组成：

1. 指向数据的指针
2. 数据类型（dtype）
3. 数组形状（shape）
4. 跨度元组（stride）：为了前进到当前维度下一个元素需要"跨过"的字节数

- 创建

1. 语法：

（1）基本方法：

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

​	参数介绍：

| object    | 数组或嵌套的数列(多维)                  |
| --------- | ------------------------------------------------------------ |
| dtype | 数组元素的数据类型                                 |
| copy  | 对象是否需要复制（没见人用过）                     |
| order | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |
| subok | 默认返回一个与基类类型一致的数组（也没见用过）           |
| ndmin | 指定生成数组的最小维度                                   |

（2）创建**0**数组：

```python
numpy.zeros(shape, dtype = float, order = 'C')
```

​	参数shape：数组形状，用**元组**，具体而言：

​	1.元组元素的个数等于数组的维度
​	2.元组中每一个元素又代表每一维度的size

其他与array相同。

（3）创建**1**数组：

```python
numpy.ones(shape, dtype = float, order = 'C')
```

​	参数与zeros使用相同。

（4）创建未初始化的数组：

```python
numpy.empty(shape, dtype = float, order = 'C')
```

​	参数与zeros使用相同。

（5）创建一个与给定数组（a）具有相同形状的**0**数组：

```python
numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
```

​	order='K'：保留输入数组的存储顺序

​	其余参数与zero使用相同。

（6）创建一个与给定数组（a）具有相同形状的**1**数组：

```python
numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)
```

​	参数与zeros_like使用相同。

（7）创建随机数数组

numpy.random模块中，有很多可以生成随机数的函数:

a. **np.random.rand(size)**：0.0到1.0

b. **np.random.randint(min,max,size,dtype)**：任意值范围内的整数。

还可以使生成随机数满足某些分布。

（8）从数值范围创建数组

```python
numpy.arange(start, stop, step, dtype)
```

构建等比和等差的还是蛮好玩的，但是用的不多就不写了。:)

2. 一些使用实例：

有的时候觉得别人教程写的不够完整，后来想想确实有的功能就是用的不多。

**创建一维数组与ones_like、zeros_like**

```python
a = np.array([1,2,3,4,5])
arr1 = np.ones_like(a)
arr2 = np.zeros_like(a)
print(a)
print(arr1)
print(arr2)
```

输出：跟list区别一下，没有逗号

```python
[1 2 3 4 5]
[1 1 1 1 1]
[0 0 0 0 0]
```

**创建二维数组**

```python
b = np.array([[1,2],[3,4]]) 
print(b)
```

输出：二维体现的还是很明显的

```python
[[1 2]
 [3 4]]
```

**创建未初始化的数组**：二维，size分别为4，3

```python
c = np.empty((4,3),dtype=int)
print(c)
```

输出：（不一定相同）

```python
[[         0          0  858993459]
 [1069757235          0 1070596096]
 [         0 1071644672          0]
 [1072168960          0 1072693248]]
```

可见未初始化不等同于全为0

**创建随机数数组**

```python
d = np.random.rand(4,4)
print(d)
e = np.random.randint(1,10,(2,4))
print(e)
```

输出：随机不唯一

```python
[[0.15682689 0.84546636 0.06570655 0.30833308]
 [0.96138934 0.69994505 0.15138579 0.79974171]
 [0.83733462 0.21990323 0.54013074 0.78474504]
 [0.24115087 0.29397448 0.88901847 0.75713048]]
[[2 7 8 8]
 [2 1 9 6]]
```
**从数值范围创建数组**

```python
arr = np.arange(2,15,3,dtype=float)
print(arr)
```

输出：

```python
[ 2.  5.  8. 11. 14.]
```

注意这个输出的小数点的含义。



- 数组属性

1. 基本概念

   **rank**：秩，数组维度

   **axis**：轴，每人一个线性的数组

2. 对象属性：a为narray

| 属性    | 说明                                 |
| ------- | ------------------------------------ |
| a.ndim  | 秩                                   |
| a.shape | 元组，每个轴上的大小，一维数组是(x,) |
| a.size  | 元素总个数                           |
| a.dtype | 元素的数据类型                       |

3. 编程举例

```python
f = np.random.rand(3,4)
print(f)
print(f"{f.ndim},{f.shape},{f.size},{f.dtype}")
```

输出：

```python
[[0.36994096 0.12480562 0.08519459 0.45437099]
 [0.42962184 0.82867576 0.84730836 0.74792832]
 [0.68490496 0.43171272 0.28655231 0.28958175]]
2,(3, 4),12,float64
```

- 数组的运算

1. 切片与索引

可以使用内置的slice函数，结果作为下标索引。也可以直接用冒号分隔。参数都是start，stop和step

编程举例：

（1）一维数组

```python
a = np.arange(10)
sli = slice(3,10,3)  #取下标为3，6，9
b = a[sli]
print(b)
b = a[3:10:3]
print(b)
```

输出：

```python
[3 6 9]
[3 6 9]
```

（2）二维数组：切片要分别对行、列做限定，中间用逗号连接。可以使用省略号...表示选择元组的长度与数组的维度相同。注意这个省略号不是shift+6,是手动敲三个点上去。

```python
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1:,0:2]) #从第1行到最后一行，每一行输出第0到第1列
print(a[0:2,…]) #从第0行到第1行，每一行都完整输出
```

输出：

```python
[[4 5]
 [7 8]]
[[1 2 3]
 [4 5 6]]
```



2. 线性代数

   比较跳跃但是确实Pytorch要用。

   NumPy 提供了线性代数函数库 **linalg**：

   （1）dot()：对于一维数组，计算对应元素的乘积和，同inner()向量内积；对于二维数组，计算矩阵乘法
```python
numpy.dot(a, b, out=None) 
```

​	out可以选择，表示把运算结果保存到哪个narray变量中，但是运算本身也可以返回结果。

​	例如：

```python
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[2,5],[6,1],[3,4]])
print(np.dot(a,b))
```

​	输出：

```python
[[23 19]
 [56 49]]
```

​	背后的逻辑是：

```python
[[1*2+2*6+3*3 1*5+2*1+3*4]
 [4*2+5*6+6*3 4*5+5*1+6*4]]
```

​	（2）vdot()：向量点积。将输入的数组展平为一维向量，然后计算对应元素的乘积之和。注意元素总数必须相等。

​	例如：

```python
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[2,5],[6,1],[3,4]])
print(np.vdot(a,b))
```

​	输出：

```python
73
```

​	背后的原理：

```python
1*2+2*5+3*6+4*1+5*3+6*4 = 2+10+18+4+15+24 = 73
```

​	（3）linalg.det()：计算输入矩阵的**行列式**。会把输入矩阵当作浮点数矩阵处理，并且使用浮点数运算。

​	例如：

```python
a = np.array([[1,2],[4,5]])
print(np.linalg.det(a))
```

​	输出：

```python
-2.9999999999999996
```

​	原理是：

```python
1*5-2*4
```
