from flask import Flask, render_template
from flask_cors import CORS
import json

from swipe import main

from model import BaseModel, BaiduModal, ZhihuModal, WeixinModal

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('template.html', data=BaseModel().select())

@app.route('/update')
def update():
    main()
    return '<h1>正在运行</h1>'

@app.route('/baidu')
def baidu():
    return render_template('baidu.html', data=BaiduModal().select())

@app.route('/zhihu')
def zhihu():
    return render_template('zhihu.html', data=ZhihuModal().select())

@app.route('/weixin')
def weixin():
    return render_template('weixin.html', data=WeixinModal().select())


if __name__ == '__main__':
  app.run()