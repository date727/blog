---
title: CUDA！——CUDA Shared Memory
published: 2025-02-07
description: ''
image: 'potato.jpg'
tags: [Study,CUDA]
category: 'CUDA'
draft: true
lang: 'zh_CN'
---

# 1D stencil(模板)

- 模板操作理念：模板映射了一个数据窗口或范围，被依次应用于数据集，以生成相应的结果。

- 模板特性：

  模板宽度：窗口/基础数据的宽度（通常为奇数）

  设想一个`宽度`为7的模板，`半径`则为3（模板中心左侧或者右侧的数据个数）

  ![](1.png)
