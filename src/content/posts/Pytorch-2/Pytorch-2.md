---
title: 学习深度学习——tensor restart!
published: 2025-02-01
description: 'Review the knowledge points of tensors.'
image: 'torch2.jpg'
tags: [Study,Python,Deep Learning,Pytorch]
category: 'Deep Learning'
draft: false 
lang: 'zh_CN'
---

之前本来是要至少把tensor学完的，学完numpy感觉人麻了，接着继续学吧。

# 手册第一章

## 1.3 60分钟快速入门 （官方）

### 张量（Tensors）

首先还是先导入：

```python
import numpy as np
import torch
```

**张量初始化**

1. 创建一个未初始化的矩阵

使用**torch.emtpy(行,列)**语句。

编程示例：构建一个5\*3的未初始化的矩阵

```python
x = torch.empty(5,3)
print(x)
```

输出：

```python
tensor([[9.9088e+27, 1.3102e-42, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00]])
```

看得出来跟narray的输出还是有区别的。

2. 创建一个随机初始化的矩阵

用到的函数如下：

| 函数                           | 功能                                   |
| ------------------------------ | -------------------------------------- |
| torch.rand(行,列)              | (行,列)的矩阵，内容为0-1的随机小数     |
| torch.randint(min,max,(行,列)) | (行,列)的矩阵，内容为min-max的随机整数 |
| torch.randn(行,列)             | (行,列)的矩阵，内容符合正态分布        |


```python
x = torch.rand(5,3)
print(x)
x = torch.randn(5,3)
print(x)
x = torch.randint(1,5,(5,3))
print(x)
```

输出：
```python
tensor([[0.8891, 0.9038, 0.4738],
        [0.5434, 0.1041, 0.0486],
        [0.9605, 0.5458, 0.9185],
        [0.7952, 0.2197, 0.4257],
        [0.8178, 0.2337, 0.0844]])
tensor([[ 0.9734, -0.5133,  0.4681],
        [-0.0463, -0.8564,  0.3412],
        [ 0.3065,  0.1255, -0.5150],
        [-0.2186,  1.2599,  1.1024],
        [ 1.6691, -0.3001,  0.3801]])
tensor([[3, 1, 1],
        [4, 1, 4],
        [3, 2, 4],
        [3, 4, 3],
        [4, 3, 2]])
```

3. 创建一个用**0**或**1**填充的矩阵

| 函数                               | 功能                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| torch.zeros(行,列)                 | (行,列)的矩阵，内容都为float类型的0                          |
| torch.ones(行,列)                  | (行,列)的矩阵，内容都为float类型的1                          |
| torch.ones_like(x_zero)         | 与x_zero对象结构相同的矩阵，内容都为float类型的1 |
| torch.rand_like(x_zero)            | 与x_zero对象结构相同的矩阵，内容为0-1的随机小数              |
| torch.randn_like(x_zero)           | 与x_zero对象结构相同的矩阵，内容符合正态分布                 |
| torch.randint_like(x_zero,min,max) | 与x_zero对象结构相同的矩阵，内容为min-max的随机整数（但是类型可能是小数，要用dtype限定） |

要注意的就是rand_like、randn_like和randint_like的使用都需要有个用0填充的向量。但是在这一点也很有疑虑就是，到处写的东西都不一样。有的说rand_like(tensor)对象就行，但是我的电脑运行起来就是报错。不过没有太多的必要在这个初始化的细节上纠结太多。同样，矩阵中的数据类型我也没有太关注，毕竟你想看看是什么直接编程print就行了。

编程示例如下：

```python
x_zero=torch.zeros(5,3)
print(x_zero)
x_ones=torch.ones(5,3)
print(x_ones)
x_ones=torch.ones_like(x_zero)
print(x_ones)
x = torch.rand_like(x_zero)
print(x)
x = torch.randn_like(x_zero)
print(x)
x = torch.randint_like(x_zero,1,10)
print(x)
```

可以得到结果：

```python
tensor([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])
tensor([[0.4962, 0.8443, 0.5706],
        [0.7028, 0.7917, 0.0519],
        [0.4328, 0.9480, 0.7444],
        [0.1028, 0.4927, 0.6412],
        [0.8281, 0.5692, 0.7954]])
tensor([[ 1.7035,  1.5930,  0.2906],
        [ 0.8667, -0.8758,  0.8929],
        [-0.5367, -0.5109,  0.0921],
        [ 0.4566,  0.4810,  1.3056],
        [ 1.0616,  0.4984, -0.7873]])
tensor([[1., 6., 7.],
        [9., 9., 1.],
        [5., 7., 9.],
        [6., 6., 5.],
        [8., 7., 4.]])
```

4. 直接使用数据创建矩阵

使用**torch.tensor(<数据>)**语句。

编程示例：构建一个3\*2的数组
```python
data = [[1,2],[3,4],[5,6]]
x_data = torch.tensor(data)
print(x_data)
```

可验证得到：

```python
tensor([[1, 2],
        [3, 4],
        [5, 6]])
```

5. 从NumPy数组初始化

使用**torch.from_numpy(np对象)**语句。

```python
x_np = torch.from_numpy(np.arange(3,10,2))
print(x_np)
```

可以得到输出：

```python
tensor([3, 5, 7, 9], dtype=torch.int32)
```



**张量属性**

假设x是tensor对象。

| 函数             | 属性     |
| ---------------- | -------- |
| x.shape/x.size() | 形状     |
| x.dtype          | 数据类型 |
| x.device         | 存储设备 |

例如：

```python
x = torch.rand(3,4)
print(f"{x.shape}")
print(f"{x.dtype}")
print(f"{x.device}")
```

得到输出：

```python
torch.Size([3, 4])
torch.float32
cpu
```



**张量操作**

张量操作可以在GPU上运行。放一个代码块在这里，因为我没有GPU(sad)

```python
if torch.cuda.is_available():
  tensor = tensor.to('cuda')
  print(f"Device tensor is stored on: {tensor.device}")
```

1. 索引与切片

跟numpy没什么不同，这里写一个案例：

```python
tensor = torch.randint(2,5,(4,4))
print(tensor)
print(tensor[1:3,1]) #取出来1-2行，第1列的数字
```

可以得到输出;

```python
tensor([[3, 3, 3, 3],
        [2, 2, 2, 2],
        [4, 3, 2, 4],
        [2, 4, 4, 4]])
tensor([2, 3])
```

2. 联接张量

可用于沿给定维度连接一系列张量。语法如下：

```python
torch.cat([tensors], dim=…)
```

对于二维数组，dim=0表示行，dim=1表示列，默认为0。编程案例如下：

```python
x = torch.randint(2,5,(4,4))
y = torch.randint(2,5,(4,4))
print(x)
print(y)
print(torch.cat([x,y], dim=1))
print(torch.cat([x,y], dim=0))
```

得到输出如下：

```python
#x的值
tensor([[4, 2, 4, 4],
        [3, 4, 4, 2],
        [4, 4, 2, 2],
        [3, 4, 4, 4]])
#y的值
tensor([[4, 4, 3, 4],
        [2, 2, 2, 2],
        [4, 2, 3, 2],
        [2, 2, 4, 3]])
#dim=1，沿着列增加的方向
tensor([[4, 2, 4, 4, 4, 4, 3, 4],
        [3, 4, 4, 2, 2, 2, 2, 2],
        [4, 4, 2, 2, 4, 2, 3, 2],
        [3, 4, 4, 4, 2, 2, 4, 3]])
#dim=0，沿着行增加的方向
tensor([[4, 2, 4, 4],
        [3, 4, 4, 2],
        [4, 4, 2, 2],
        [3, 4, 4, 4],
        [4, 4, 3, 4],
        [2, 2, 2, 2],
        [4, 2, 3, 2],
        [2, 2, 4, 3]])
```

3. 矩阵乘法

（1）自乘，只给定一个tensor。实现方式有两种：

```python
tensor.mul(tensor)
tensor * tensor
```

（2）两个矩阵相乘，涉及到广播的问题，放个[链接](https://blog.csdn.net/didi_ya/article/details/121158666)在这里，先把numpy的广播捋清楚了再看。若两个tensor都是一维的，则返回两个向量的点积运算结果；若两个tensor都是二维的，则返回两个矩阵的矩阵相乘结果。语法如下：

```python
torch.matmul(x,y)
x @ y
```

编程举例如下：

```python
x = torch.randint(1,3,(3,))
y = torch.randint(1,3,(3,))
print(x)
print(y)
print(torch.matmul(x,y))
x = torch.randint(1,3,(2,2))
y = torch.randint(1,3,(2,2))
print(x)
print(y)
print(torch.matmul(x,y))
```

得到输出：

```python
tensor([2, 1, 2])
tensor([2, 1, 1])
tensor(7)
tensor([[2, 2],
        [1, 1]])
tensor([[1, 1],
        [2, 2]])
tensor([[6, 6],
        [3, 3]])
```

**替换**

任何 以``_`` 结尾的操作都会用结果替换原变量。

**与Numpy的转换**

Torch Tensor与NumPy数组共享底层内存地址，修改一个会导致另一个的变化。

1. 将一个Torch Tensor转换为NumPy数组

使用**tensor.numpy()**。编程举例如下：

```python
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
```

可以得到输出：

```python
tensor([1., 1., 1., 1., 1.])
[1. 1. 1. 1. 1.]
```
相互影响的体现：(接着上面)

```python
a.add_(1)
print(a)
print(b)
```

可以得到输出：

```python
tensor([1., 1., 1., 1., 1.])
[1. 1. 1. 1. 1.]
tensor([2., 2., 2., 2., 2.])
[2. 2. 2. 2. 2.]
```

2. 将一个NumPy数组转换为Torch Tensor

在前面的初始化讲了。

这一章就是整理的比较潦草，基础部分就不弄得那么多，免得头重脚轻。