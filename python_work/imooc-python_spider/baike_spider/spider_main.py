#_*_ coding:gbk _*_
'''
Created on 2018��4��3��

@author: Administrator
'''
from baike_spider import url_manage, html_downloader, html_parser, html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manage.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()
        
        #����ĵ��ȳ���
    def craw(self,root_url):
        count = 1
        #����ʼ��url��ӵ�url������
        self.urls.add_new_url(root_url)
        #�ж��Ƿ���δ��ȡurl
        print("start")
        while self.urls.has_new_url():
            
            #���쳣����
            try:
                #��ȡһ������ȡurl
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count,new_url))
                print("1")
                #print(new_url)
                
                #��������������ҳ�沢���浽html_cont��
                html_cont = self.downloader.download(new_url)
                print("2")
                
                #���ý���������ҳ��õ��µ�url������
                #print("new_url:" + new_url)
                #print("html_cont:" + str(html_cont))
                new_urls,new_data = self.parser.parse(new_url,html_cont)#�������д����������ݣ���ǰ��ȡ��url�Ѿ�ҳ������
                print("3")
                
                #�������õ���url��ӵ�url������
                self.urls.add_new_urls(new_urls)
                print("4")
                
                #�ռ�����
                self.outputer.collect_data(new_data)
                print("5")
                
                if count == 1000:
                    break
                
                count += 1
                print("6")
            except:
                print("craw failed")
            
        #����ռ��õ�����
        self.outputer.output_html()
            
        

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)