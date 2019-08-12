from db import DB

def get_db():
    return DB()


class BaseModel:
    def __init__(self, tablename='Weibo'):
        self.tablename = tablename
        self.create()

    def create(self):
        with get_db() as db:
            exists = db.execute("select count(name) from sqlite_master where type = 'table' and name = '{0}'".format(self.tablename))
            if exists.fetchone()[0] == 1:
              pass
            else:
              db.execute('''CREATE TABLE {}
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       TITLE    TEXT    NOT NULL,
       CONTENT  TEXT     NOT NULL,
       URL      CHAR(200),
       CREATEDATE TIMESTAMP default (datetime('now', 'localtime')));'''.format(self.tablename))

    def insert(self, data):
        with get_db() as db:
            _exists = self.get_id(data[0])
            if len(_exists) > 0:
              return
            else:
              db.execute("INSERT INTO {0} (TITLE,CONTENT,URL) \
      VALUES {1}".format(self.tablename, data))

    def select(self):
        with get_db() as db:
           result = db.execute("SELECT * from {0} ORDER BY CREATEDATE DESC".format(self.tablename)).fetchall()
        _r = []
        for row in result:
          _r.append({
            'id': row[0],
            'title': row[1],
            'content': row[2],
            'url': row[3],
            'create_date': row[4]
          })
        return _r

    def update(self, id, data):
        with get_db() as db:
            db.execute("UPDATE {0} SET CONTENT = '{2}' WHERE ID={1}".format(self.tablename, id, data))

    def delete(self):
        with get_db() as db:
            db.execute("DELETE FROM {0};".format(self.tablename))

    def get_id(self, title):
        with get_db() as db:
           result = db.execute("SELECT id from {0} where TITLE = '{1}'".format(self.tablename,title)).fetchall()
        _r = []
        for row in result:
          _r.append({
            'id': row[0]
          })
        return _r

class BaiduModal(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, tablename='Baidu')


class ZhihuModal(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, tablename='Zhihu')


class WeixinModal(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, tablename='Weixin')

if __name__ == '__main__':
    model = BaseModel()
    model.create()