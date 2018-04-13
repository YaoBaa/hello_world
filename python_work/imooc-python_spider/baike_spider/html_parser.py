#_*_ coding:gbk _*_
'''
Created on 2018年4月3日

@author: Administrator
'''
#解析器代码
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class HtmlParser(object):
    
    def get_new_urls(self,page_url,soup):
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            print(new_full_url)
            new_urls.add(new_full_url)
        print(new_urls)
        return new_urls
        
    def get_new_data(self,page_url,soup):
        res_data = {}
        
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title">
        #<h1>Python</h1>
        title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title".find("h2"))
        if title_node is None:
            print("title_node is None")
            return
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summery_node = soup.find("div",class_="lemma-summary")
        res_data['summery'] = summery_node.get_text()
        print(res_data)
        
        return res_data
        
        
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is  None:
            print("page_url is None or html_cont is not None")
            return
         
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls = self.get_new_urls(page_url,soup)
        new_data = self.get_new_data(page_url,soup)
        return new_urls,new_data
        
    
    
