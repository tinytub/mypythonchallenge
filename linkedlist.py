#!/usr/bin/env python
import urllib2
import re
getsrc = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').read()
getnum = "".join(re.findall('1\d*',getsrc))
#print getnum
#print 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % getnum
def getlink(getnum):
    while True:
        if getnum:
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % getnum
            #url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % 66831
            getsrc = urllib2.urlopen(url).read()
            getnum = "".join(re.findall('\d*$',getsrc))
            #if not getnum:
            #    break
            print getnum
            print getsrc
        elif url:
            getnum = int("".join(re.findall('\d*',url))) / 2
        else:
            break
    #return getnum,getsrc
    return getsrc

print getlink(getnum)
