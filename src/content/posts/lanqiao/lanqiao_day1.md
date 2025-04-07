---
title: 搞点python778——day1
published: 2025-01-23
description: 'a brief introduction to sys'
image: 'lanqiao_1.jpg'
tags: [Study,Python,sys]
category: 'Python'
draft: false 
lang: 'zh_CN'
---

- [开始准备蓝桥杯吧！](#开始准备蓝桥杯吧)
- [标准库sys](#标准库sys)
  - [脚本?](#脚本)
  - [sys：解释器的状态、参数以及和外界的交互](#sys解释器的状态参数以及和外界的交互)

# 开始准备蓝桥杯吧！
u1s1感觉python学到一半现在重新拿起来的感觉真的很不好受……类都没学到，我恨医学……
总是要开始的，就成为我的第二篇博客8。
# 标准库sys
有看到过但是似乎没什么影响就没搞懂的东西，今天好好搞明白。
>“sys”即“system”，“系统”之意。该模块提供了一些接口，用于访问 Python 解释器自身使用和维护的变量，同时模块中还提供了一部分函数，可以与解释器进行比较深度的交互。

Let's start.

## 脚本?

脚本是一段用于自动化执行特定任务的**代码**，可以帮助我们自动化处理日常任务，提高工作效率。与传统的编译语言不同，脚本语言不需要编译，直接在解释器中运行。这使得脚本更加灵活和易于修改。

写这段的时候主播其实并不会脚本（）只是想看看Python写脚本与正常的.py有什么不同。查了看，确实是没什么不同（）所以怎么写脚本之后再学，好吗？好的。

## sys：解释器的状态、参数以及和外界的交互

写几个感觉能用上的，platform那些有点像儿童编程（bushi）

1. sys.argv：列表对象，获取命令行参数

   - 从命令行运行 Python 脚本时，可以向脚本传递参数，这些参数会被存储在 `sys.argv` 中，实现从程序外部向程序传递参数。

   - `sys.argv[0]` 通常是脚本的名称；

     `sys.argv[1]` 及之后的元素是传递给脚本的实际参数。

   比方说写个py文件如下（代码也放在仓库里面了）：

   ```python
   import sys
   print(sys.argv)
   print(sys.argv[0])
   print(sys.argv[1])
   ```

   在命令行中输入：
   ```
   python argv_try.py c++ golang
   ```

   argv_try.py为文件名，c++与 golang为实际参数。可以看到输出：
   ```
   ['argv_try.py', 'c++', 'golang']
   argv_try.py
   c++
   ```

2. sys.exit()：退出当前程序

   可设置退出状态码，方便外部程序根据状态码判断程序执行结果。我们结合random库的使用编写py代码如下：

   ```python
   import sys
   import random
   num = random.randint(0, 1)
   if num!= 0:
       print("{}".format(num))
       sys.exit(1)
   print("{}".format(num))
   sys.exit(0)
   ```

   num是随机生成0或1，如果num=1，输出1，状态码为1；num=0，输出0，状态码为0

   多次运行程序可以看到两种情况：

   num=1时：

   ```
   1
   
   进程已结束，退出代码为 1
   ```

   num=0时：

   ```
   0
   
   进程已结束，退出代码为 0
   ```

3. **sys.stdin：标准输入通道**

   使用sys.stdin.readline()可以实现标准输入

   - 输入格式：默认输入的格式是字符串，需要其他类型可以强制转换；

   - 换行结束：这个方法会从标准输入中读取一行文本，直至遇到换行符 `\n`为止，并且**会把换行符也包含在返回的字符串**里。如果不需要这个换行符，可以使用 `strip()` 或 `rstrip()` 方法去除；

   - 空格结束：利用 `split()` 方法按空格对读取的字符串进行分割。如果有其他的分割需求也可以写在括号中；

   - 文件结束：当接收到 EOF 时，`sys.stdin.readline()` 会返回一个空字符串。
     例如对于输入：

   ```
   Jack
   99 85
   ```

   99、85分别代表Jack的两部门成绩，要求我们用两个变量存储并输出。
   我们编写代码如下：

   ```python
   import sys
   name=sys.stdin.readline().strip()
   grades=sys.stdin.readline().strip()
   grade1=int(grades.split()[0])
   grade2=int(grades.split()[1])
   print("{}:{} {}".format(name,grade1,grade2))
   ```

   得到输出：

   ```
   Jack:99 85
   ```

   在参赛过程中如果每次都写那么长一段还是太费时间了，所以可以在每个程序的开头写上两行：
   ```python
   import sys
   input = lambda:sys.stdin.readline().strip()
   ```

   这才是主播突发奇想学习这个的原因啊啊啊啊（）*因为这个看上去真的太帅了*

   lambda的的作用是将input映射到sys.stdin.readline().strip()，之后可以直接使用input，**注意不要在里面写提示词**。比方说：

   ```python
   import sys
   input = lambda:sys.stdin.readline().strip()
   num = int(input())
   print("{}".format(num))
   ```

   输出就是输出的整数值，就不演示了。

4. stdout：标准输出
   - 相比之下print的使用更加方便，对性能有更高的需求的时候可以用；
   - sys.stdout.write()：输出字符串，需要手动添加换行符（大型巨婴）；
   - sys.stdout.flush()：程序输出的数据往往先存储在一个叫做缓冲区的内存区域里，等缓冲区满了或者满足某些条件时被一次性输出到终端。sys.stdout.flush() 的作用就是强制把缓冲区里的数据立即输出到终端。主要用于在需要实时看到输出结果的场景中。
   我们编写代码如下：
   ```python
   import sys
   lines=["25%","50%","75%","100%"]
   for i in lines:
    sys.stdout.write(i)
    sys.stdout.write('\n')
    sys.stdout.flush()
   ```
   
   得到输出：
   ```
   25%
   50%
   75%
   100%
   
   ```
   
   没想到写博客这么累啊（）其实本来要写os的但是真没想到（）比赛过程中用的也不多就先放着吧。好吗？好的。
