#! /usr/bin/env python
import pickle
import re
import urllib2
#gettext = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
f = open('banner.p')
#for line in pickle.load(f):
#        for x in line:
#            print ''.join(x[0] * x[1])

for line in pickle.load(f):
        print ''.join([x[0] * x[1] for x in line])
f.close()
