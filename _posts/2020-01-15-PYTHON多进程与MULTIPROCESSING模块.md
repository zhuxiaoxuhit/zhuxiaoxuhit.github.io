---
layout:     post
title:      PYTHON多进程与MULTIPROCESSING模块
subtitle:   MULTIPROCESSING
date:       2020-01-15
author:     朱晓旭
header-img: img/bg.jpg
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
![gil](img/gil.jpg)

## multiprocessing.Process简要介绍
multiprocessing 是一个用与 threading 模块相似API的支持产生进程的包。 multiprocessing 包同时提供本地和远程并发，使用子进程代替线程，有效避免 Global Interpreter Lock 带来的影响。     
#### class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)      
>group 应该始终是 None ；它仅用于兼容 threading.Thread 。 target 是由 run() 方法调用的可调用对象。它默认为 None ，意味着什么都没有被调用。 name 是进程名称（有关详细信息，请参阅 name ）。 args 是目标调用的参数元组。 kwargs 是目标调用的关键字参数字典。如果提供，则键参数 daemon 将进程 daemon 标志设置为 True 或 False 。如果是 None （默认值），则该标志将从创建的进程继承。

#### 类的方法：
>`start()`
>启动进程活动。   
`join([timeout])`
>如果可选参数 timeout 是 None （默认值），则该方法将阻塞，直到调用 join() 方法的进程终止。一个进程可以被 join 多次。进程无法join自身，因为这会导致死锁。  
`is_alive()`
>返回进程是否还活着。  
`daemon`
>守护进程的标志，一个布尔值。这必须在 start() 被调用之前设置。  
`close()`
关闭 Process 对象，释放与之关联的所有资源。  

#### 例子
通过创建一个 Process 对象然后调用它的 start() 方法来生成进程。 Process 和 threading.Thread API 相同。   
```python
from multiprocessing import Process  
def f(name):   
	print('hello', name,'!')       
if __name__ == '__main__':        
	p = Process(target=f, args=('zhuxiaoxu',))     
	p.start()   
	p.join()    
```

## Join
join的作用是阻塞主进程（主进程等待p进程执行完毕，才继续执行），和多线程一样。python 默认参数创建线程后，不管主线程是否执行完毕，都会等待子线程执行完毕才一起退出，有无join结果一样。join方法有一个参数是timeout，即如果主线程等待timeout，子线程还没有结束，则主线程强制结束子线程。

#### 例子




### 参考

- [官方文档](https://umap-learn.readthedocs.io/en/latest/index.html)
- [源码](https://github.com/lmcinnes/umap)
- [论文](https://arxiv.org/pdf/1802.03426.pdf)
- [报告](https://www.youtube.com/watch?v=nq6iPZVUxZU&frags=pl%2Cwn)


