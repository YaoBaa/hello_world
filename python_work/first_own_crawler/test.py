#_*_ coding:utf-8 _*_

import pymysql
from bs4 import BeautifulSoup
from urllib import request
import re


conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='first_own_crawler',
    charset='utf8'
)

cursor = conn.cursor()


# new_url = 'https://baike.baidu.com/item/Python'
# resp = request.urlopen(new_url).read().decode('utf-8')#打开并读取网页
# soup = BeautifulSoup(resp, 'html.parser')#解析网页
# url_lists = soup.find_all('a')
# for url_list in url_lists:
#     print(url_list.get_text(), '--->', url_list.get('href', 'not exist'), '\n')  # 有href,则输出，没有href，则输出'not exist()'
#     print(url_list)

data = 'txtName.\'Text = \\\\"\\"txtMath.\Text = \"\"txtEN.Text = \"\"'

def cha(match):
    val = match.group()
    num = "\\" + val
    return num

data_1 = re.sub(r'[\'\\]', cha, data)  # add中的参数为正则表达式在str4中匹配到的值
datas = re.sub(r'[\"]', cha, data_1)  # add中的参数为正则表达式在str4中匹配到的值
print(data)
print(datas)


str1 = '"qq'
str2 = '.com"'
str3 = str1 + str2
print(str3)
print(len('https://baike.baidu.com/item/%E5%85%B3%E4%BA%8E%E5%BB%BA%E5%9B%BD%E4%BB%A5%E6%9D%A5%E5%85%9A%E7%9A%84%E8%8B%A5%E5%B9%B2%E5%8E%86%E5%8F%B2%E9%97%AE%E9%A2%98%E7%9A%84%E5%86%B3%E8%AE%AE'))

# resp = request.urlopen('https://baike.baidu.com/item/史记2016?fr=navbar')
# print("史记")



