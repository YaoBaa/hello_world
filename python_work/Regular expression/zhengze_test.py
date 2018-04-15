#_*_ coding:utf-8 _*_

import re

str1 = 'imooc python'
print(str1.find('on'))
print(str1.startswith('imooc'))


#正则表达式
pa = re.compile(r'imooc')
print(pa)
print(type(pa))
ma = pa.match(str1)
print(ma)
print('\n')

ma = re.match(r'[\w]', '0Gmyac')
print(ma.group())

ma = re.match(r'\[[\w]\]', '[r]')
print(ma.group())

ma = re.match(r'[A-Z][a-z]*', 'Aadsfasdfasdfa')#*作用于[a-z]，匹配0次或者无限次
print(ma.group())

ma = re.match(r'[_a-zA-Z]*[_\w]*', '_dfa324123412341234')
print(ma.group())

ma = re.match(r'[1-9]?[0-9]', '0')
print(ma.group())

ma = re.match(r'^[1-9][0-9]{4,9}@qq[.]com$', '1085865354@qq.com')#.放在[]里面表示只能匹配.，否则为匹配任意单个字符
print(ma.group())

ma = re.match(r'\Aimoc?\w*', 'imooocpython')#?只作用在了c上面
print(ma.group())

print('\n')

ma = re.match(r'[1-9]?\d$|0\w*', '011sdfg1')
print(ma.group())

ma = re.match(r'\w{4,10}@(qq|sina|163)[.]com', 'yao72396@163.com')
print(ma.group())

ma = re.match(r'<(\w+>)\w+</\1', '<book>python</book>')
#ma = re.match(r'<(\w+>)\w+</\1', '<book>python</b123ook>') #错误写法，\1必须要和前面括号匹配的字符串完全一致
print(ma.group())

ma = re.match(r'<(?P<name>\w+>)\w+</(?P=name)', '<book>python</book>')#括号内的?P<name>表示给分组取名，(?P=name)引用分组,同样要完全一致
print(ma.group())


print('\n')

str1 = 'imooc videonum = 1000'
info = re.search(r'\d+', str1)
print(info.group())

str2 = 'c++ = 100,java = 90,python = 80'
info = re.findall(r'\d+', str2)#查找所有
print(info)
print(sum([int(x) for x in info]))

str3 = 'c++ = 100,java = 100,python = 100'
info = re.sub(r'\d+', '90', str3)#全部替换
print(info)
print(str3)
print('\n')

if True:#为了把相关代码放在一起，
    def add1(match):
        val = match.group()
        num = int(val) + 1
        return str(num)
    str4 = 'c++ = :100,java = 100,python = 100'
    info = re.sub(r'\d+', add1, str3)#add中的参数为正则表达式在str4中匹配到的值
    print(info)

spl = re.split(r':| ', str4)#对字符串进行分割
print(spl)





