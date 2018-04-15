#_*_ coding:utf-8 _*_
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

#获取文件对象
fp = open('cc17_lecture03.pdf', 'rb')

#创建一个与文档关联的解释器
parser = PDFParser(fp)

#创建PDF文档对象
doc = PDFDocument()

#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize('')

#创建PDF资源管理器
resource = PDFResourceManager()

#参数分析器
laparam = LAParams()

#创建一个聚合器
device = PDFPageAggregator()










