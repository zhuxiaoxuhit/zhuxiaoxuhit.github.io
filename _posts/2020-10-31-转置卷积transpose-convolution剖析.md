---
layout:     post
title:      转置卷积剖析 
subtitle:   Transpose Convolution 
date:       2020-12-24
author:     朱晓旭
header-img: img/bg.jpg
catalog: true
tags:
    - conv transpose1d 
    - transpose conv 
---
# 问题
之前遇到过多次转置卷积的运算，查了就忘，这次在PQMF算法C语言实现过程中，对转置卷积采用矩阵乘加速，就详细记录下来分析过程。这里采用语音领域常用的一维转置卷积为例，高维会更简单。

# 一维转置卷积矩阵乘分析
### 输入输出信信息
```
input: [batch size, input channel, input length]
weight(kernel): [output channel, input channel, kenel size]
output: [batch size, output channel, outputs length]
```
Torch转置卷积语句(以Torch为例)
```
y = torch.nn.functional.conv_transpose1d(x,f,stride)
```

### 实例分析
我们给出以下参数:
```
input: [1,4,8]
weight: [4,4,4]
output: [1,4,32]
stride = 4
```

首先分析卷积过程(from output to input):
```
[8,4(stride)] x [4(kenel_size),1] -> [8,1]
input channel=4可得：
[8,16(stride, input channel)] x [16(input channel, kernel size),1] -> [8,1]
output channel=4可得：
[8,16(stride,input channel)] x [16(input channel, kenrnel size),4(output channel)] -> [8,4]
```
转置卷积为卷积的逆运算，因此,from input to output:
```
[8,4]x[4,16] -> [8,16]
```

### 代码
```python
import torch
import torch.nn.functional as F
import numpy as np

#x = torch.from_numpy(x).view(1, 1, -1).float()
x = np.array([1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16,1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16]).astype(np.float32).reshape(8,4)
filters= np.array([1., 0., 0., 0., 0., 0., 0., 0.,0., 0., 0., 0.,0., 0., 0., 0.,0., 0., 0., 0.,1., 0., 0., 0.,0., 0., 0., 0.,0., 0., 0., 0.,0., 0., 0., 0.,0., \
        0., 0., 0.,1., 0., 0., 0.,0., 0., 0., 0.,0., 0., 0., 0., 0., 0., 0., 0.,0., 0., 0., 0.,1., 0., 0., 0.]).astype(np.float32).reshape(4,16)
y = x.dot(filters)
print(y)

xx = torch.from_numpy(x).view(1, 4, 8).float()
ff = torch.from_numpy(filters).view(4, 4, 4).float()
yy = F.conv_transpose1d(xx,ff,stride=4)
print(yy.numpy())

```

