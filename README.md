﻿

baidu-push 百度云推送API
---

**写在前面**  

>官方页面上推荐的API有一年没更了，编码方式也不对胃口。  
同时还不支持 Python3。正好用到，于是自写一个，当前只实现了一个 push_msg 接口，  
不过基本上90%时间有这个就足够了。  
另外也欢迎大家向这里提交代码来完善其他的接口，如果我自己用到也会加上的。  


**依赖**
* requests


**特性**  

* 简单易读，结构清晰  
* 同时支持 py2 和 py3  
* 使用 ujson 代替官方 json（如果你安装了的话）  

**许可协议**  
* zlib license  

**历史**

* 2014-05-16 - 0.1, fy  
