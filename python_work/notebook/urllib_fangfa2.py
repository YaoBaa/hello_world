#coding=utf-8
import urllib.request

url = 'https://www.baidu.com'
#����Request����
request = urllib.request.Request(url)

#�������
request.add_data('a','1')

#���http��header
request.add_header('User-Agent','Mozilla/5.0')

#���������ȡ���
response = urllib.request.urlopen(request)
