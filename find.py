#!/usr/bin/env python
import re
file = open('/project/test/html.txt')
text = file.read()
#reg = re.compile('\w')
patt = r'(\w+)'
final = re.findall(patt,text)
#print text
#final = re.sub('\{|\}|\[|\]|\_|\+|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)','',text)
print final
file.close()

