#_*_ coding:gbk _*_
'''
Created on 2018年4月3日

@author: Administrator
'''

import pymysql


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, url, data):
        if data is None:
            print('data is none')
            return
        print('2222222222222222222')
        conn = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='baidubaike',
            charset='utf8'
        )

        try:
            cursor = conn.cursor()
            sql = 'insert into pythonbk(title,bi) values("'+url+'","'+str(data['summery'])+'")'
            # print(url)
            # print(data['summery'])

            cursor.execute(sql,)


            conn.commit()
            # self.datas.append(data)
        finally:
            # cursor.close()
            conn.close()
        
    
    # def output_html(self):
    #     fout = open('output.html','w')
    #
    #     fout.write('<html>')
    #     fout.write('<body>')
    #     fout.write('<table>')
    #
    #     for data in self.datas:
    #         fout.write("<tr>")
    #         fout.write("<td>%s</td>" % data['url'])
    #         # fout.write("<td>%s</td>" % data['title'].encode('gbk'))
    #         fout.write("<td>%s</td>" % data['summery'].encode('utf-8'))
    #         fout.write("</tr>")
    #
    #     fout.write('</table>')
    #     fout.write('</body>')
    #     fout.write('</html>')
    #
    #     fout.close()
    
    
    
    



