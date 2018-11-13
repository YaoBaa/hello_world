#_*_ coding:utf-8 _*_

import sys
sys.setrecursionlimit(100)
def move(n, a, b, c):
#把所有盘子当做两个来看，最底下的和上面的，不管最后最上面的
#盘子移动到了哪里都把它所处的位置当做a位置带进此方法中。 
    if n == 1:
        print(a + ' --> ' + c)
    #将上面的盘子运到b
    move(n-1, a, c, b)
    print(a + ' --> ' + b)
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
