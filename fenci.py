import jieba
import jieba.analyse
from model import BaseModel, BaiduModal, ZhihuModal, WeixinModal

def get_data():
    weibo = BaseModel().select()[:10]
    baidu = BaiduModal().select()[:10]
    zhihu = ZhihuModal().select()[:10]
    weixin = WeixinModal().select()[:10]
    return "".join([x.get('title') for x in weibo+baidu+zhihu+weixin])

def fenci():
    data = get_data()
    tags = jieba.analyse.extract_tags(data, topK=100, withWeight=True)
    # for v, n in tags[:5]:
    #     print(v,n)
    return ",".join([v for (v, n) in tags[:5]])

if __name__ == "__main__":
    print(fenci())
