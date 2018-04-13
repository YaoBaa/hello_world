#_*_ coding:gbk _*_
'''
Created on 2018年4月3日

@author: Administrator
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    
    def output_html(self):
        fout = open('output.html','w')
        
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('gbk'))
            fout.write("<td>%s</td>" % data['summary'].encode('gbk'))
            fout.write("</tr>")
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        
        fout.close()
    
    
    
    



