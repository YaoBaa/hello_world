#_*_ coding:gbk _*_
'''
Created on 2018��4��3��

@author: Administrator
'''
import url_manage, html_downloader, html_parser, html_output


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
                print('craw %d : %s' % (count, new_url))
                #print(new_url)
                
                #��������������ҳ�沢���浽html_cont��
                html_cont = self.downloader.download(new_url)
                
                #���ý���������ҳ��õ��µ�url������
                #print("new_url:" + new_url)
                #print("html_cont:" + str(html_cont))
                new_urls,new_data = self.parser.parse(new_url,html_cont)#�������д����������ݣ���ǰ��ȡ��url�Ѿ�ҳ������
                
                #�������õ���url��ӵ�url������
                self.urls.add_new_urls(new_urls)
                #�������ݵ����ݿ�
                self.outputer.collect_data(new_url, new_data)
                
                if count == 2000:
                    break
                
                count += 1
            except:
                print("craw failed")
            
        #����ռ��õ�����
        # self.outputer.output_html()
            
        

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
