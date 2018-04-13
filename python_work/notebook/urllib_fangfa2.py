#coding=utf-8
import urllib.request

url = 'https://www.baidu.com'
#创建Request对象
request = urllib.request.Request(url)

#添加数据
request.add_data('a','1')

#添加http的header
request.add_header('User-Agent','Mozilla/5.0')

#发送请求获取结果
response = urllib.request.urlopen(request)
