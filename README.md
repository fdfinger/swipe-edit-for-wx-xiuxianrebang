# swipe-edit-for-wx-xiuxianrebang
> 修仙热榜微信订阅号内容爬取

## 安装

``` shell
pip install -i https://pypi.douban.com/simple flask flask_cors requests BeautifulSoup4 
```

## 运行

``` shell
python www.py
```

## 数据抓取

1. 使用命令行

``` shell
python swipe.py
```

2. 使用已经启动的url

[点我](http://127.0.0.1/update)

## 文章编辑

1. 打开[135编辑器](https://www.135editor.com/)

2. 运行`python www.py`并且打开 [localhost](http://localhost:5000)
3. 选中页面，复制
4. 135编辑器 粘贴进去
5. 样式调整一下就OK了
6. 【135编辑器】-->【微信复制】
7. 微信打开，光标在内容编辑上，将复制好的内容粘贴进去
8. 保存
9. 选择模版，发送或者定时发送

