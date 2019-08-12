import time
import requests
from bs4 import BeautifulSoup


from model import BaseModel, BaiduModal, ZhihuModal, WeixinModal

db = BaseModel()
baidu_db = BaiduModal()
zhihu_db = ZhihuModal()
weixin_db = WeixinModal()

def get(url):
    header_info = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
    return requests.get(url, headers=header_info).text

def weibo():
    weibo = "https://s.weibo.com/top/summary/"
    html = get(weibo)
    if not html:
      return
    soup = BeautifulSoup(html)
    new_list = [x for x in soup.find_all('a') if '/weibo?q=' in x.get('href')]
    for new in new_list[:10]:
      #newdata = "{0},{1},{2}".format()
      db.insert((new.text, '', new.get('href')))
      weibo_detail(new.text, new.get('href'))

def weibo_detail(title, url):
    weibo_detail_url = "https://s.weibo.com" + url
    time.sleep(5)
    html = get(weibo_detail_url)
    if not html:
      return
    weibo_detail_soup = BeautifulSoup(html)
    content = weibo_detail_soup.find_all('div', attrs={"class":"content"})
    try:
        ids = db.get_id(title)
        db.update(ids[0].get('id'), content[0].find_all('p', attrs={"class":"txt"})[0].text)
    except:
      pass

def baidu():
    baidu_url = "http://top.baidu.com/buzz?b=1"
    html = get(baidu_url)
    if not html:
      return
    soup = BeautifulSoup(html.encode("iso-8859-1").decode('gbk').encode('utf8'))
    fliter_baidu = soup.find_all('a', attrs={"class":"list-title"})
    for new in fliter_baidu[:10]:
      baidu_db.insert((new.text, '', new.get('href')))
      baidu_detail(new.text, new.get('href'))
    del baidu_url
    del html
    del soup
    del fliter_baidu

def baidu_detail(title, url):
    baidu_detail_url = url
    time.sleep(5)
    html = get(baidu_detail_url)
    if not html:
      return
    baidu_detail_soup = BeautifulSoup(html)
    filter_baidu_detail = baidu_detail_soup.find_all("div",attrs={"class":"c-row"})
    try:
        ids = baidu_db.get_id(title)
        baidu_db.update(ids[0].get('id'), filter_baidu_detail[0].text)
    except:
      pass


def zhihu():
    zhihu_url = "https://tophub.today/n/mproPpoq6O"
    html = get(zhihu_url)
    if not html:
      return
    soup = BeautifulSoup(html)
    fliter_zhihu = soup.find_all('td', attrs={"class":"al"})
    for new in fliter_zhihu[:10]:
      zhihu_db.insert((new.a.text, '', new.a.get('href')))
      zhihu_detail(new.a.text, new.a.get('href'))
    del zhihu_url
    del html
    del soup
    del fliter_zhihu

def zhihu_detail(title, url):
    zhihu_detail_url = url
    time.sleep(5)
    html = get(zhihu_detail_url)
    if not html:
      return
    zhihu_detail_soup = BeautifulSoup(html)
    filter_zhihu_detail = zhihu_detail_soup.find_all("div",attrs={"class":"RichContent RichContent--unescapable"})
    try:
        ids = zhihu_db.get_id(title)
        zhihu_db.update(ids[0].get('id'), filter_zhihu_detail[0].text)
    except:
      pass

# https://tophub.today/n/WnBe01o371

def weixin():
    weixin_url = "https://tophub.today/n/WnBe01o371"
    html = get(weixin_url)
    if not html:
      return
    soup = BeautifulSoup(html)
    fliter_weixin = soup.find_all('td', attrs={"class":"al"})
    for new in fliter_weixin[:10]:
      weixin_db.insert((new.a.text, '', new.a.get('href')))
      #weixin_detail(new.a.text, new.a.get('href'))
    del weixin_url
    del html
    del soup
    del fliter_weixin

def main():
    weibo()
    baidu()
    zhihu()
    weixin()

if __name__ == '__main__':
    weixin()