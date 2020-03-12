---
layout:     post
title:      Cheat Sheet
subtitle:   Mathematical formula
date:       2020-03-12
author:     朱晓旭
header-img: img/bg.jpg
catalog: true
tags:
    - math
    - CNN
    - LSTM
    - GRU
    - Attention	
---

## LSTM
<center>$$\boldsymbol{I}_t = \sigma(\boldsymbol{X}_t \boldsymbol{W}_{xi} + \boldsymbol{H}_{t-1} \boldsymbol{W}_{hi} + \boldsymbol{b}_i)$$</center>
<center>$$\boldsymbol{F}_t = \sigma(\boldsymbol{X}_t \boldsymbol{W}_{xf} + \boldsymbol{H}_{t-1} \boldsymbol{W}_{hf} + \boldsymbol{b}_f)$$</center>
<center>$$\boldsymbol{O}_t = \sigma(\boldsymbol{X}_t \boldsymbol{W}_{xo} + \boldsymbol{H}_{t-1} \boldsymbol{W}_{ho} + \boldsymbol{b}_o)$$</center>
<center>$$\tilde{\boldsymbol{C}}_t = \text{tanh}(\boldsymbol{X}_t \boldsymbol{W}_{xc} + \boldsymbol{H}_{t-1} \boldsymbol{W}_{hc} + \boldsymbol{b}_c)$$</center>
<center>$$\boldsymbol{C}_t = \boldsymbol{F}_t \odot \boldsymbol{C}_{t-1} + \boldsymbol{I}_t \odot \tilde{\boldsymbol{C}}_t$$</center>
<center>$$\boldsymbol{H}_t = \boldsymbol{O}_t \odot \text{tanh}(\boldsymbol{C}_t)$$</center>
##  GRU
<center>$$\boldsymbol{R}_t = \sigma(\boldsymbol{X}_t \boldsymbol{W}_{xr} + \boldsymbol{H}_{t-1} \boldsymbol{W}_{hr} + \boldsymbol{b}_r)$$</center>
<center>$$\boldsymbol{Z}_t = \sigma(\boldsymbol{X}_t \boldsymbol{W}_{xz} + \boldsymbol{H}_{t-1} \boldsymbol{W}_{hz} + \boldsymbol{b}_z)$$</center>
<center>$$\tilde{\boldsymbol{H}}_t = \text{tanh}(\boldsymbol{X}_t \boldsymbol{W}_{xh} + \left(\boldsymbol{R}_t \odot \boldsymbol{H}_{t-1}\right) \boldsymbol{W}_{hh} + \boldsymbol{b}_h)$$</center>
<center>$$\boldsymbol{H}_t = \boldsymbol{Z}_t \odot \boldsymbol{H}_{t-1}  + (1 - \boldsymbol{Z}_t) \odot \tilde{\boldsymbol{H}}_t$$</center>
##  Attention
<center>$$\boldsymbol{c}_{t'} = \sum_{t=1}^T \alpha_{t' t} \boldsymbol{h}_t$$</center>
<center>$$\alpha_{t' t} = \frac{\exp(e_{t' t})}{ \sum_{k=1}^T \exp(e_{t' k}) },\quad t=1,\ldots,T$$</center>
<center>$$e_{t' t} = a(\boldsymbol{s}_{t' - 1}, \boldsymbol{h}_t)$$</center>
e.g.
<center>$$a(\boldsymbol{s}, \boldsymbol{h}) = \boldsymbol{v}^\top \tanh(\boldsymbol{W}_s \boldsymbol{s} + \boldsymbol{W}_h \boldsymbol{h})$$</center>
##  CNN
#### 2D 
Input:10*10*3(长*宽*输入维度)     
Filters(output channel or滤波器数量or输出维度or输出深度):4            
kernel size(卷积核尺寸):4*4                    
Stride:1         
Weights:4*4*3*1(卷积核尺寸*输入维度*输出维度)             
Output:10*10*4("SAME") or (10-4+1)*(10-4+1)*4("VALID")           
![](cc_cnn3.png)         
#### 1D
Input:8*3(句子帧数*每帧的维度)        
Filters(output channel or滤波器数量or输出维度or输出深度):2        
kernel size(卷积核尺寸):4          
Stride:1         
Weights:4*3*2(卷积核尺寸*输入维度*输出维度)         
Output:8*2("SAME") or (8-4+1)*2("VALID")             
![](cc_cnn4.PNG) 
#### 语音技术中常用的1D技法:concat不同卷积核大小的输出结果
Input:7*5(句子帧数*每帧的维度)         
Filters(output channel or滤波器数量or输出维度or输出深度):for i in 2,2,3,3,4,4       
kernel size(卷积核尺寸):1           
Stride:1       
Weights:2*5*1,2*5*1,3*5*1,3*5*1,4*5*1,4*5*1(卷积核尺寸*输入维度*输出维度)       
Max pooling and the first time concat 0utput:2*1,2*1,2*1     
After second concat:6*1            
Output:2*1                
![](cc_cnn5.jpg)
#### 参考
- [pytorch之nn.Conv1d详解](https://www.cnblogs.com/pythonClub/p/10421799.html)



