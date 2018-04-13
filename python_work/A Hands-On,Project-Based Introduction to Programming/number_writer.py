#coding=utf-8
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json' #指出文件存储的数据为JSON格式
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj) #将数字列表存储在文件numbers.json中
