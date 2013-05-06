#!/usr/bin/env python
import re
import zipfile

f = open('90052.txt').read()
zf = zipfile.ZipFile('channel.zip')
getnum = ''.join(re.findall('\d*$',f))
#print getnum
#f.close()
comm = []
def getlink(getnum):
    while True:
        if getnum:
            fname = '%s.txt' % getnum
            f = open(fname).read()
            comm.append(zf.getinfo(fname).comment)
            getnum = ''.join(re.findall('\d*$',f))
           # f.close()
            #print f
            #print getnum
            #getcom = ''.join(re.findall('"""(.*?)"""',f,re.S))
            #print getcom
        else:
            break
    return f,getnum,comm

print ''.join(getlink(getnum)[2])
