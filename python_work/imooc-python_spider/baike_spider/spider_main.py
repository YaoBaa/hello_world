#_*_ coding:gbk _*_
'''
Created on 2018年4月3日

@author: Administrator
'''
import url_manage, html_downloader, html_parser, html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manage.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()
        
        #爬虫的调度程序
    def craw(self,root_url):
        count = 1
        #将初始的url添加到url管理器
        self.urls.add_new_url(root_url)
        #判断是否有未爬取url
        print("start")
        while self.urls.has_new_url():
            
            #做异常处理
            try:
                #获取一个待爬取url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                #print(new_url)
                
                #启动下载器下载页面并保存到html_cont中
                html_cont = self.downloader.download(new_url)
                
                #调用解析器解析页面得到新的url和数据
                #print("new_url:" + new_url)
                #print("html_cont:" + str(html_cont))
                new_urls,new_data = self.parser.parse(new_url,html_cont)#解析器中传入两个数据，当前爬取的url已经页面数据
                
                #将解析得到的url添加到url管理器
                self.urls.add_new_urls(new_urls)
                #保存数据到数据库
                self.outputer.collect_data(new_url, new_data)
                
                if count == 2000:
                    break
                
                count += 1
            except:
                print("craw failed")
            
        #输出收集好的数据
        # self.outputer.output_html()
            
        

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
