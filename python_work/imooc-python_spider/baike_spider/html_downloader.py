#_*_ coding:gbk _*_
'''
Created on 2018��4��3��

@author: Administrator
'''
import urllib.request

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        print("download is ok")
        return response.read()
        
    
    



