---
layout:     post
title:      PYTHON多进程与MULTIPROCESSING模块
subtitle:   MULTIPROCESSING
date:       2020-01-15
author:     朱晓旭
header-img: img/bg.png
catalog: true
tags:
    - python
    - python multiprocessing
    - python multithreading
    - GIL
    - 进程间通信	
---


## python多线程与GIL（Global Interpreter Lock） 
>python多进程多线程是个古老的话题了，最近翻到之前自己写的文档，顺手摘录到博客上了。  
python的全局解释器锁使得任意时刻只有一个线程在真正运行，所以呢，可以讲它是"假多线程"。他能对脚本的提速仅仅体现在IO操作中，因为IO操作是可以和线程并行的，所以它节省了IO操作时间。正是由于它的GIL锁的出现，才有了本场multiprocessing的解说。
![gil](img/gil.gif)










### 参考

- [官方文档](https://umap-learn.readthedocs.io/en/latest/index.html)
- [源码](https://github.com/lmcinnes/umap)
- [论文](https://arxiv.org/pdf/1802.03426.pdf)
- [报告](https://www.youtube.com/watch?v=nq6iPZVUxZU&frags=pl%2Cwn)


