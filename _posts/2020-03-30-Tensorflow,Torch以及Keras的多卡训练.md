---
layout:     post
title:      Tensorflow,Torch以及Keras的多卡训练
subtitle:   Multi-GPU Training of Tensorflow,Torch and Keras
date:       2020-03-30
author:     朱晓旭
header-img: img/bg.jpg
catalog: true
tags:
    - Multi-GPU
    - Tensorflow
    - Torch
    - Keras
    - 数据并行(单机多卡)
---
# 多卡训练
数据并行：不同的GPU输入不同的数据，运行相同的完整的模型。 
每个GPU上的batch_size为总的batch_size除以卡数。     
优点：最突出的是加快训练。其他的之后再补充。
指定某个可见：CUDA_VISIBLE_DEVICE = 0

# Torch
#### 单卡
指定卡号后把模型和数据存到gpu中。
```python
device= torch.device("cuda:0")
net.to(device)
```
#### 多卡
```python
device= torch.device("cuda")
net =nn.DataParallel(net,device_ids=[2,3])
net.to(device)
```

# Tensorflow
#### tensorflow-gpu指定cpu训练
cpu只有一块，只能是0号
```python
with tf.device('/cpu:0'):
	v1 = tf.constant([1.0, 2.0, 3.0], shape=[3], name='v1')
	v2 = tf.constant([1.0, 2.0, 3.0], shape=[3], name='v2')
	sumV12 = v1 + v2
    
	with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
		print sess.run(sumV12)
```
#### tensorflow-gpu指定某一gpu训练
相当于CUDA_VISIBLE_DEVICE = 3
```python
with tf.device('/gpu:3'):
	v1 = tf.constant([1.0, 2.0, 3.0], shape=[3], name='v1')
	v2 = tf.constant([1.0, 2.0, 3.0], shape=[3], name='v2')
	sumV12 = v1 + v2
    
	with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
		print sess.run(sumV12)
```
#### tensorflow-gpu多卡训练
tf.distribute.MirroredStrategy 是一种简单且高性能的，数据并行的同步式分布式策略，主要支持多个 GPU 在同一台主机上训练。使用这种策略时，我们只需实例化一个 MirroredStrategy 策略:    
```python
strategy = tf.distribute.MirroredStrategy()
```
并将模型构建的代码放入 strategy.scope() 的上下文环境中:
```python
with strategy.scope():
	# 模型构建代码
```
可以在参数中指定设备，如:
```python
strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"])
```
即指定只使用第 0、1 号 GPU 参与分布式策略。     

wiki中的例子：
<pre>
import tensorflow as tf
import tensorflow_datasets as tfds

num_epochs = 5
batch_size_per_replica = 64
learning_rate = 0.001

strategy = tf.distribute.MirroredStrategy()
	#输出设备数量
	print('Number of devices: %d' % strategy.num_replicas_in_sync)  
	batch_size = batch_size_per_replica * strategy.num_replicas_in_sync

# 载入数据集并预处理
def resize(image, label):
	image = tf.image.resize(image, [224, 224]) / 255.0
	return image, label

# 使用 TensorFlow Datasets 载入猫狗分类数据集，详见“TensorFlow Datasets数据集载入”一章
dataset = tfds.load("cats_vs_dogs", split=tfds.Split.TRAIN, as_supervised=True)
dataset = dataset.map(resize).shuffle(1024).batch(batch_size)

with strategy.scope():
	model = tf.keras.applications.MobileNetV2()
	model.compile(
	optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
	loss=tf.keras.losses.sparse_categorical_crossentropy,
	metrics=[tf.keras.metrics.sparse_categorical_accuracy]
	)

model.fit(dataset, epochs=num_epochs)
</pre>

# Keras
数据并行包括在每个设备上复制一次目标模型，并使用每个模型副本处理不同部分的输入数据。Keras 有一个内置的实用函数 keras.utils.multi_gpu_model，它可以生成任何模型的数据并行版本，在多达 8 个 GPU 上实现准线性加速。    
<pre>
from keras.utils import multi_gpu_model

# 将 `model` 复制到 8 个 GPU 上。
# 假定你的机器有 8 个可用的 GPU。
parallel_model = multi_gpu_model(model, gpus=8)
parallel_model.compile(loss='categorical_crossentropy',optimizer='rmsprop')

# 这个 `fit` 调用将分布在 8 个 GPU 上。
# 由于 batch size 为 256，每个 GPU 将处理 32 个样本。
parallel_model.fit(x, y, epochs=20, batch_size=256)
</pre>



