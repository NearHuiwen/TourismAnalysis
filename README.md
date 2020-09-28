TourismAnalysis携程旅游景点爬虫分析
===============

> 项目普及技术：MongoDB、pylab、线程锁

请在Python3下运行(版本太低可能会出现不兼容，本人用的是3.7版本)

运行前请配置好MongoDB相关数据


## 注意

大家好，首先该项目的思路来源是（来自于https://www.jb51.net/article/160836.htm）“详解Python 爬取13个旅游城市，告诉你五一大家最爱去哪玩？”

（本人做了一些修改，原作者信息来源是“qunar”网站，个人认为数据不符本人需求，改为“携程”），感谢贵作者的慷慨开源

（截止版本2020年9月28日，即后面可能接口出现更新，可能会过时，请谅解）

这是本人一个闲时**练手项目**，源码仅作为和大家一起**学习Python**使用，你可以免费: 拷贝、分发和派生当前源码（最后最好添加一些自己的见解）。但你不可以用于*商业目的*及其他*恶意用途*。



服务端对抓取的一些限制，如抓取频率、IP等等，如果你遇到了这样的问题，
可能你的下载量已经超出了**学习目的**，对此我也拒绝支持并表示非常抱歉。



## 开发环境安装

首先，配置好你的Python、MongoDB环境

本人用的是pipenv虚拟环境
如果你已有虚拟环境以下可忽略
安装
```bash
$ pip install -i https://pypi.douban.com/simple pipenv
```
创建文件夹“TourismAnalysis”（项目放在这里）
创建虚拟环境
```bash
$ cd TourismAnalysis
$ pipenv install
```

进入虚拟环境
```bash
$ cd TourismAnalysis
$ pipenv shell
```



导入项目，也可直接下载覆盖TourismAnalysis文件夹
```bash
$ git clone https://github.com/NearHuiwen/TourismAnalysis.git
```


大功告成,直接跳到下一节配置和运行.

## 配置和运行

首先部署MongoDB数据库
如下图：

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/p1.png" width="300">

创建4个集合

（分别：

dom_products：国内景点
ove_products：国外景点
domesticcities：国内城市
overseascities：国外城市
）

在db_manager_mongo.py 配置MongoDB账号和密码

## 运行步骤：

1、运行city_spider.py 爬取相关城市信息，用于爬取景点接口使用

2、运行product_spider.py 爬取步骤1中城市的景点信息

3、运行analysis_ly.py 分析展示步骤2的景点信息

## 分析展示如下：

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a2.jpg" width="700">

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a3.png" width="700">

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a4.jpg" width="700">

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a5.png" width="700">

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a6.jpg" width="700">

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a7.png" width="700">

<img src="https://raw.githubusercontent.com/NearHuiwen/TourismAnalysis/master/picture/a8.png" width="700">