#coding=utf-8
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json' #ָ���ļ��洢������ΪJSON��ʽ
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj) #�������б�洢���ļ�numbers.json��
