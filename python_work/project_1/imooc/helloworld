#_*_ coding:utf-8 _*_

from urllib import request
from urllib import parse


req = request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
postData = parse.urlencode([
    ("StartStation","a7a04c89-900b-4798-95a3-c01c455622f4"),
    ("EndStation","977abb69-413a-4ccf-a109-0272c24fd490"),
    ("SearchDate","2018/04/11"),
    ("SearchTime","18:00"),
    ("SearchWay","DepartureInMandarin")
])
req.add_header('Origin','http://www.thsrc.com.t')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
resp = request.urlopen(req)
resp_read = resp.read().decode("utf-8")
print(resp_read)