#_*_ coding:gbk _*_
'''
Created on 2018,4,3,

@author: Administrator
'''

import urllib.request
import http.cookiejar


url = 'https://www.baidu.com'

print('First��һ��')
response1 = urllib.request.urlopen(url)#��������
print(response1.getcode())#״̬�룬200���ʾ����ɹ�
print(len(response1.read()))

print('\nSecond�ڶ���')
request = urllib.request.Request(url)
request.add_header('user-agent','Mozilla/5.0')#������αװ�������
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('\nThird������')
cj = http.cookiejar.CookieJar()#���ȴ���cookie����
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)#��urllib��װopener�����ʱ��urllib������cookie�������ǿ����
response3 = urllib.request.urlopen(url)#��������
print(response3.getcode())#״̬�룬200���ʾ����ɹ�
print(cj)
print(response3.read())

