---
layout:     post
title:      期望最大算法
subtitle:   Expectation-maximization algorithm
date:       2020-03-30
author:     朱晓旭
header-img: img/bg.jpg
catalog: true
tags:
    - 期望最大算法
    - EM算法
    - 隐变量
    - 最大似然估计
---
# 思路
当使用最大似然估计通过X样本点数据集进行参数$\theta$的估计时，如果模型中存在隐变量z。
原来的MLE是：
<center>\theta_{MLE}=arg\max_{\theta}p(X|\theta)</center>
现在有了隐变量z，则MLE是：
<center>\theta_{MLE}=arg\max_{\theta}\sum_{z \in{Z}}p(X,z|\theta)</center>
观测数据的似然没有直接的表达式，必须通过隐变量来计算，这意味着不能直接进行极大似然估计。
如果我们知道每个样本对应的隐变量，那么可以直接通过极大似然估计得到样本生成的过程，即模型参数。
问题的关键是我们不知道每个样本对应的隐变量，只能去大概地估计。这个估计的过程就是为每个样本分配它由每个隐变量生成的概率，即后验概率。
跟真实的完整数据相比，后验概率将每个样本分成了若干份，这样我们就获得了另一种形式的"完整数据"。把一个样本X分成若干份，每份贡献一部分对数似然，这个样本的对数似然是每部分对数似然之和：
<center>\sum_{z \in{Z}}p(X,z|\theta^old)ln(x,z|\theta)</center>


本质：
因数据缺失而不能直接使用MLE方法的时候(MLE在数学上是解方程；数理统计上是叫极大似然；概率论叫条件概率。数学上没有解析解)，
我们可以用这个缺失数据的期望值来代替缺失的数据，而这个缺失的数据期望值和它的概率分布有关。那么我们可以通过对似然函数关于缺失数据期望的最大化，来逼近原函数的极大值。

### 参考
- [机器学习-周志华](https://github.com/Mikoto10032/DeepLearning/blob/master/books/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%91%A8%E5%BF%97%E5%8D%8E.pdf)
- [统计学习方法-李航](http://www.dgt-factory.com/uploads/2018/07/0725/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95.pdf)
