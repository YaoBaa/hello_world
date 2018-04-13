#_*_ coding:gbk _*_
'''
Created on 2018,4,3,

@author: Administrator
'''

import urllib.request
import http.cookiejar


url = 'https://www.baidu.com'

print('First第一种')
response1 = urllib.request.urlopen(url)#发送请求
print(response1.getcode())#状态码，200则表示请求成功
print(len(response1.read()))

print('\nSecond第二种')
request = urllib.request.Request(url)
request.add_header('user-agent','Mozilla/5.0')#把爬虫伪装成浏览器
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('\nThird第三种')
cj = http.cookiejar.CookieJar()#首先创建cookie容器
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)#给urllib安装opener，这个时候urllib就有了cookie处理的增强能力
response3 = urllib.request.urlopen(url)#发送请求
print(response3.getcode())#状态码，200则表示请求成功
print(cj)
print(response3.read())

