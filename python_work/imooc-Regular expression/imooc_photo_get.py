#_*_ coding:utf-8 _*_

from bs4 import BeautifulSoup as bsbs
from urllib import request
import re
import pymysql

resp = request.urlopen('https://www.imooc.com/').read().decode('utf-8')

soup = bsbs(resp, 'html.parser')
# print(soup)
lists = soup.find_all('img')


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='baidubaike',
    charset='utf8'
)
try:
    cursor = conn.cursor()
    sql = 'insert into photo(url) values(%s)'
    for list in lists:
        print(list)
        list1 = list['src']
        if re.search(r'/.+[.]jpg', list1):
            list_save = list1[2:]
        if re.search(r'/.+[.]png', list1):
            list_save = 'https://www.imooc.com/' + list1
        cursor.execute(sql, list_save)
    conn.commit()

    sql = 'select url from photo'
    cursor.execute(sql)
    urllists = cursor.fetchall()
    for url in urllists:
        print(url)

finally:
    cursor.close()
    conn.close()

