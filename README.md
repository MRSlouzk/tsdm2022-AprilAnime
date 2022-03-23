# tsdm2022-AprilAnime
一个获取天使动漫2022年4月新番排名的爬虫(使用xpath检索)

## 使用方法    
1.安装python 3.8环境并确保自己配置好了  
2.安装lxml库  
3.进入https://www.tsdm39.net/forum.php?mod=viewthread&tid=1093323 并打开开发者模式，进入"网络"窗口，点击第一个'forum.php......'，在右侧的"请求标头"中复制自己的cookie  
4.将cookie复制入headers变量中的cookie键的值中(就是'cookie':' ' 后面的单引号当中，并确保你的cookie数据放在了同一行，否则会报错)  
5.运行py程序(没有魔法的话需要挺长时间的)  
