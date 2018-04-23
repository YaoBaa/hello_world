#_*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
from urllib import request
import re

class UrlParser():
    def parser(self,new_url):
        print(new_url)
        resp = request.urlopen(new_url).read().decode('utf-8')#打开并读取网页
        soup = BeautifulSoup(resp, 'html.parser')#解析网页
        urls = self.get_urls(new_url, soup)
        datas = self.get_datas(new_url, soup)
        return urls,datas



    #获取新的url列表
    def get_urls(self,new_url,soup):
        new_urls = set()
        url_lists = soup.find_all('a')
        for url_list in url_lists:
            to_url = url_list.get('href', 'not exist')
            if re.search('/item/', to_url):
                to_end_url = 'https://baike.baidu.com' + to_url
                new_urls.add(to_end_url)
        print(new_urls)
        return new_urls

    #获取想要的数据
    def get_datas(self,new_url,soup):
        data = ''
        new_datas = {}
        new_datas['url'] = new_url

        #获取词条简介
        brief_intr = soup.find('div',class_='lemma-summary')
        if brief_intr == None:
            return new_datas
        brief_intro = brief_intr.get_text()
        def cha(match):
            val = match.group()
            num = "\\" + val
            return num
        brief_intros = re.sub(r'[\'\"\\]', cha, brief_intro)  # cha中的参数为正则表达式在brief_intro中匹配到的值
        new_datas['brief_intr'] = brief_intros

        #获取词条名称
        name = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_datas['name'] = name
        print(name)

        #获取词条全部详细信息
        infos = soup.find_all('div', class_='para')
        for info in infos:
            data += info.get_text()
        #数据中会出现"无法保存到数据库，进行转义
        def cha(match):
            val = match.group()
            num = "\\" + val
            return num
        datas = re.sub(r'[\'\"\\]', cha, data)  # cha中的参数为正则表达式在data中匹配到的值
        #将转义后的字符串存入字典
        new_datas['info'] =datas
        print(new_datas)
        return new_datas


