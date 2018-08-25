#!/usr/bin/env python
#
#
#

import urllib

def go(a,b,c):
    per=100.0 * a * b /c
    if per>100:
        per=100
    #print "%.2f%%" % per
    print "a=",a
    print "b=",b
    print "c=",c

url="https://ss1.bdstatic.com/5aAHeD3nKgcUp2HgoI7O1ygwehsv/media/ch1000/png/1111.png"
local="a.png"
urllib.urlretrieve(url,local,go)

