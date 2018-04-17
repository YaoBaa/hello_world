#_*_ coding:utf-8 _*_

import pymysql

class UrlData():
    def save_datas(self,url,datas):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='first_own_crawler',
            charset='utf8'
        )
        cursor = conn.cursor()

        if 'brief_intr' not in datas.keys():
            return
        else:
            sql = 'insert into datas(url,title,brief,info) values("%s","%s","%s","%s")'\
                    %(url,datas['name'],datas['brief_intr'],datas['info'])
            cursor.execute(sql)
            conn.commit()

        cursor.close()
        conn.close()
