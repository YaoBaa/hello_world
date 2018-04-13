from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, 'html.parser')
#
# print(soup.prettify())#按照标准的缩进格式的结构输出
# print('\n')
# print(soup.title)
# print(soup.title.name)
# print('\n')
#
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.find_all('a'))#以数组形式返回
# for link in soup.find_all('a'):
#     print(link.string)
#
# print(soup.find('p', {'class': 'story'}).string)#class为story的标签
# print(soup.find('p', {'class': 'story'}).get_text())#一个P标签中有多个文本，用get_text()，否则.string结果为None
#
# print(soup.find(id='link2'))


for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

print(soup.find_all('a', href=re.compile(r"^http://example.com")))
