---
layout:     post
title:      SOX
subtitle:   SOX：the Swiss Army knife of audio manipulation
date:       2020-03-24
author:     朱晓旭
header-img: img/bg.jpg
catalog: true
tags:
    - sox
    - audio manipulation
    - 音频处理  
---


# 简介

SOX-音频处理转换和处理工具中的瑞士军刀。在音频处理方面命令简洁且高效，配合xargs命令能方便的进行小批量音频数据的处理。能实现如下的功能   
1.  单音频的处理：音频的播放速度，采样率，音量，声道数量等。
2.  多音频的合并等。
3.  soxi查看音频文件meta信息。
4.  play播放音频。

sox命令处理流程：    
Input(s) -> Combiner -> Effects -> Output(s)

sox命令的格式：
官方文档给出的：
```console
sox [global-options] [format-options] infile1                     

[[format-options] infile2] ... [format-options] outfile               

[effect [effect-options]] ...       

```
我们比较常用的处理单个文件的指令格式：
```console
sox  infile  format  outfile   effect
```

参数(Gain用来表示信号的强度，是音频输入信号和输出信号差异的幅度,gain 控制的是「进入」声音设备的信号,volume是声音大小（响度）的值,volume控制的是从声音设备「输出」的声响大小.将 Gain 理解为对信号的调整，将 Volume 理解为处理完成后声音响度的听觉感受)：     
```console
SPECIAL FILENAMES (infile only):                       
"|program [options] ..." 使用管道             
http://server/file       使用音频文件的url作为输入文件（URL支持需要wget是可用的）             

GLOBAL OPTIONS (gopts) (在第一个effect之前的任意位置):            
--buffer BYTES， 	 sox处理音频的时候的缓存字节数。            
--clobber                当输出文件文件名已经存在默认会进行重写覆盖。            
--combine concatenate    Concat音频(-m是mix，-M是merge，-T是multiply)                
--dft-min NUM            Minimum size (log2) for DFT processing (default 10)              
--effects-file FILENAME  File containing effects and options             
-G，--guard		 使用gain effect来防止音频截幅或者截频或者响度norm时超过限制造成失真。例子sox −G infile −b 16 outfile rate 44100 dither −s              
--i, --info              和soxi相同                    
-m, -M，-T               -m是mix，-M是merge，-T是multiply                   
--norm[dB-level]	 自动的使用gain effect防止失真并且响度归一化音频。                               
-S，--show-progress	 显示处理的音频的meta信息以及已经处理的百分比。                  
-V[level]		 设置打印在终端的信息。0是没有信息打印，1是仅错误被打印，2警告也会被打印，3包括描述信息等都被打印，4所有信息都被打印            

FORMAT OPTIONS (fopts):输出文件将尽可能与输入文件具有相同的格式，并且不会被包括提供输出格式选项在内的各种方式所覆盖。                     
-v|--volume FACTOR       调整音频音量的大小。                              
--ignore-length          忽略头文件给的音频长度信息；读到结束标志EOF为止                        
-t|--type FILETYPE       音频类型(wav,mp3,flac等等)。self-describing格式（如 WAV、FLAC、MP3）的文件包含一个用于描述信号和编码属性的文件头，而raw或headless格式的音频则不包含这些信息。            
-e|--encoding ENCODING   采样点的编码格式(ENCODING may be one of signed-integer,unsigned-integer, floating-point, mu-law, a-law,ima-adpcm, ms-adpcm, gsm-full-rate)                 
-b|--bits BITS           位深(一个采样点用几个bit保存)                   
-N|--reverse-nibbles     nibble是半个byte(4bit)。                       
-X|--reverse-bits        Encoded bit-order                 
--endian little|big|swap Encoded byte-order; swap means opposite to default             
-L/-B/-x                 Short options for the above              
-c|--channels CHANNELS   声道数; e.g. 1=mono 2 = stereo           
-r|--rate RATE           采样率            
-C|--compression FACTOR  Compression factor for output format             
--no-glob                Don't `glob' wildcard match the following filename               

EFFECTS:                        
pitch[-q]shift [segment [search [overlap]]] 	改变音频的pitch音高。                 
spectrogram 					画声谱图。-y是声谱图的y轴最大长度，-m是灰度。比如 -y  129  -m -r            
```




# 常用命令
#### 音频格式转换
- sox自动读取音频文件的后缀名，并进行格式转换。a是mp3格式的文件，转换为b是wav格式的文件。
```console
sox a.mp3 b.wav
```

- sox把mp3格式转换为wav格式，并且附加effects:b.wav保存为单通道mono,16k采样率,音频淡入特效fade-in，normalization，并且保位深16bit.
```console
sox a.mp3 −b 16 b.wav channels 1 rate 16k fade 3 norm
```

- sox把二进制文件(无header信息)转换为wav文件，格式选项为：采样率为16k，有符号8bit整数，单通道。注意把raw文件转为其他格式需要指名格式，因为raw为二进制文件，不含有meta信息。(可理解为np.fromfile需要指明文件类型)
```console
sox −r 16k −e signed −b 8 −c 1 voice-memo.raw voice-memo.wav
```
#### 添加音频效果
- 把音频速度调整为原来的1.027倍
```console
sox slow.wav fixed.wav speed 1.027
```

- 把音量调整为原来的1.027倍
```console
sox a.wav b.wav volume 1.027
sox a.wav -v 1.027 b.wav
```
- 为避免截幅，可以通过 -n stat 命令获取音量增大的最大限制。
```console
sox a.wav -n stat -v | xargs -I {} sox a.wav b.wav volume {}
```
- 按照百分比调整音高
```console
sox a.wav b.wav pitch -31
```

-  sox 命令的 -M 选项将左右两个声道的单声道音频合并成一个双声道文件
```console
sox -M left.wav right.wav stereo.wav
```

- 对双声道文件中两个声道的均一化处理，将其输出为单声道音频：
```console
sox original.wav mono.wav channels 1
```

- 提取双声道音频文件中单个声道的数据并作为单声道音频输出,下面提取第二个声道(若是双声道则是指右声道) 或者融合多个声道(实例中融合前三个声道)。
```console
sox stereo.wav channel_2.wav remix 2
sox stereo.wav channel_2.wav remix 1,2,3
```

- 画声谱图(a.wav的第一个声道采样率10k，y轴长度129，输出为a.png)
```console
sox  a.wav -n remix 1 rate 10k spectrogram  -y  129  -m -r -o  a.png
```

#### 合并音频(-m)

- concat两个文件.
```console
sox short.wav long.wav longer.wav
```

- 合并混合music.mp3和voice.wav并保存成mixed.flac,合并音频（两个单声道混合后是双声道）
```console
sox −m music.mp3 voice.wav mixed.flac
```

#### 获取文件meta信息(soxi 或者 sox --i)
- soxi 或 sox --i 命令可以通过解析音频文件的文件头，获取其元数据（如通道数，采样率，位深，持续时间，比特率等）。
```console
base [zhuxiaoxu@gpu66 wav_input]$ soxi multilingual_000000.wav
Input File     : 'multilingual_000000.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:14.11 = 225796 samples ~ 1058.42 CDDA sectors
File Size      : 459k
Bit Rate       : 260k
Sample Encoding: 16-bit Signed Integer PCM
```

- sox inputfile -n stat命令获取某音频文件的统计信息
```console
(base) [zhuxiaoxu@gpu66 wave]$ sox 000030.wav -n stat 
Samples read:             83600
Length (seconds):      5.225000
Scaled by:         2147483647.0
Maximum amplitude:     0.272766
Minimum amplitude:    -0.356537
Midline amplitude:    -0.041885
Mean    norm:          0.036391
Mean    amplitude:    -0.000011
RMS     amplitude:     0.056870
Maximum delta:         0.456573
Minimum delta:         0.000000
Mean    delta:         0.013225
RMS     delta:         0.028709
Rough   frequency:         1285
Volume adjustment:        2.805
```


### 参考

- [官方文档](http://sox.sourceforge.net/sox.html)





