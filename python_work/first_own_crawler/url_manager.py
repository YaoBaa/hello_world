#_*_ coding:utf-8 _*_

import pymysql

class UrlManager():
    #创建连接，供后面需要的每一个方法使用
    def con(self):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='first_own_crawler',
            charset='utf8'
        )
        return conn

    #获取new_url表的行数
    def check_new_urls(self):
        conn = self.con()
        cursor = conn.cursor()

        sql = 'select newurl from newurls'
        cursor.execute(sql)
        num = cursor.rowcount
        print("new_urls:" + str(num))

        cursor.close()
        conn.close()
        return num

    #获取old_url的行数
    def check_old_urls(self):
        conn = self.con()
        cursor = conn.cursor()


        sql = 'select oldurl from oldurls'
        cursor.execute(sql)
        num = cursor.rowcount
        print("old_urls:" + str(num))

        cursor.close()
        conn.close()
        return num

    #将用户输入的第一个url放入数据库
    def add_new_url(self, url):
        conn = self.con()
        cursor = conn.cursor()

        sql = 'insert into newurls(newurl) values("' + url +'")'
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()

    #将从网页获取到的url放入数据库
    def add_new_urls(self, urls):
        conn = self.con()
        cursor = conn.cursor()

        #建立一个set()，去除重复的url。
        # new_urls = set()
        # for url in urls:
        #     new_urls.add(url)
        #查看url是否已经在数据库中，如果在，丢弃。如果不在，放入数据库。
        for url in urls:
            sql1 = 'select id from newurls where newurl="' + str(url) + '"'
            cursor.execute(sql1)
            num = cursor.rowcount
            if num != 0:
                continue

            sql2 = 'select id from oldurls where oldurl="' + str(url) + '"'
            cursor.execute(sql2)
            num = cursor.rowcount
            if num != 0:
                continue

            sql3 = 'select id from trourls where trourl="' + str(url) + '"'
            cursor.execute(sql3)
            num = cursor.rowcount
            if num != 0:
                continue

            sql4 = 'insert into newurls(newurl) values("' + str(url) +'")'
            cursor.execute(sql4)

        conn.commit()
        cursor.close()
        conn.close()

    #从数据库中获取新的url供后续使用
    def get_new_url(self):
        conn = self.con()
        cursor = conn.cursor()

        sql = 'select newurl from newurls limit 1'
        cursor.execute(sql)
        urls = cursor.fetchone()
        for url in urls:
            print("craw:%s"%url)

        cursor.close()
        conn.close()
        return url

    #将爬完的url从newurls中移动到oldurls
    def new_url_change(self,url):
        conn = self.con()
        cursor = conn.cursor()

        sql1 = 'delete from newurls where newurl="' + url + '"'
        sql2 = 'insert into oldurls(oldurl) values("' + url + '")'
        cursor.execute(sql1)
        cursor.execute(sql2)

        conn.commit()
        cursor.close()
        conn.close()

    #将爬虫中出现问题的url存放到trourls中
    def save_url(self,url):
        conn = self.con()
        cursor = conn.cursor()

        sql1 = 'delete from newurls where newurl="' + url + '"'
        sql2 = 'insert into trourls(trourl) values("' + url + '")'
        cursor.execute(sql1)
        cursor.execute(sql2)

        conn.commit()
        cursor.close()
        conn.close()
