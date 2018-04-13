#_*_ coding:utf-8 _*_


from urllib import request
from bs4 import BeautifulSoup
import re

#请求URL，创建对象，使用utf-8编码
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


