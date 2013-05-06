#!/usr/bin/env python
import re
import urllib2
geturl = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
text = re.findall(r'<!--(.*?)-->',geturl,re.S)
wd = re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',text[0])
print wd
final = "".join(wd)
#print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text[0]))
print final
