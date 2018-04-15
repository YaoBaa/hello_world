#_*_ coding:utf-8 _*_


from urllib import request
from bs4 import BeautifulSoup
import pymysql
import re

#请求URL，创建对象，使用utf-8编码
main_url = 'https://baike.baidu.com'
resp = request.urlopen('https://baike.baidu.com/item/Python/407313?fr=aladdin').read().decode('utf-8')

#指定解析器
soup = BeautifulSoup(resp, 'html.parser')
#print(soup)

#查找所有'a'标签
list_url = soup.find_all('a')
# print(list_url)
for url in list_url:
    print(url)
    # if 'href' in url:
    print(url.get_text(), '--->', url.get('href', 'not exist'), '\n')#有href,则输出，没有href，则输出'not exist()'
#     url_1 = url["href"]
    conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='baidubaike',
        charset='utf8'
    )
    try:
        with conn.cursor() as cursor:
            # sql = 'insert into urls(urlname,urlhref) values(%s,%s)'
            # cursor.execute(sql, (url.get_text(), url.get("href", "not exist")))
            sql = 'insert into urls(urlname,urlhref) values("' + url.get_text() + '","' \
                + url.get("href", "not exist") + '")'
            if re.search(r'/item/', sql):
                sql1 ='insert into urls(urlname,urlhref) values("' + url.get_text() + '","' \
                +main_url+url.get("href", "not exist") + '")'
                cursor.execute(sql1)
                conn.commit()
    finally:
        conn.close()


