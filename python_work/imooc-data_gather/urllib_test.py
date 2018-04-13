from urllib import request


req = request.Request("http://www.baidu.com")
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
resp = request.urlopen(req)
resp_read = resp.read().decode("utf-8")
print(resp_read)