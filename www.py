from flask import Flask, render_template
from flask_cors import CORS
import json

from swipe import main

from model import BaseModel, BaiduModal, ZhihuModal, WeixinModal

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('template.html',
        weibo_data=BaseModel().select()[:10],
        baidu_data=BaiduModal().select()[:10],
        zhihu_data=ZhihuModal().select()[:10],
        weixin_data=WeixinModal().select()[:10]
    )

@app.route('/update')
def update():
    main()
    return '<h1>正在运行</h1>'

@app.route('/baidu')
def baidu():
    return render_template('baidu.html', data=BaiduModal().select()[:10])

@app.route('/zhihu')
def zhihu():
    return render_template('zhihu.html', data=ZhihuModal().select()[:10])

@app.route('/weixin')
def weixin():
    return render_template('weixin.html', data=WeixinModal().select()[:10])


if __name__ == '__main__':
  app.run()