#_*_ coding:utf-8 _*_

import url_manager
import url_parser
import url_data

class Crawler():
    def __init__(self):
        self.manager = url_manager.UrlManager()
        self.parser = url_parser.UrlParser()
        self.data = url_data.UrlData()

    def craw(self):

        count = 1
        while count <= number:
            try:
                #首先从url表里获取新的url
                new_url = self.manager.get_new_url()

                print("craw%s:"%(count) + new_url)

                #对新的url进行解释并获取其中的数据
                urls,datas = self.parser.parser(new_url)

                #将获取到的新url存入数据库
                self.manager.add_new_urls(urls)

                #将数据存入数据库
                self.data.save_datas(new_url,datas)

                #将new_url从new_urls中删除，放入到old_urls中。
                self.manager.new_url_change(new_url)
            except:
                #将出现问题的url放入到tro_urls中
                self.manager.save_url(new_url)
            finally:
                count += 1

#先执行主程序
if __name__ =="__main__":
    #先输入本次程序运行要获取的页面数
    num = input("Please enter the number that you want to get:")
    number = int(num)

    url_m = url_manager.UrlManager()
    new_urls_num = int(url_m.check_new_urls())
    old_urls_num = int(url_m.check_old_urls())

    #判断若old_urls表中有数据，new_urls表中无数据，程序直接结束。
    if old_urls_num != 0 and new_urls_num == 0:
        exit(0)
    #若old_urls表和new_urls表都无数据，则接收网页作为第一个网页。并将网页加入到new_url表中
    if old_urls_num == 0 and new_urls_num == 0:
        root_url = input("Please input the word you want to begin:")
        root_full_url = 'https://baike.baidu.com/item/' + root_url
        url_m.add_new_url(root_full_url)
    #若new_urls表中有数据，则直接进入循环，不用if语句，

    #创建一个crawler对象
    crawler = Crawler()
    #开始公共部分的主程序
    crawler.craw()