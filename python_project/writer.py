import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

tree=ET.parse('stream.xml')
root=tree.getroot()

f=open('streamdata.xml','w')

for i in range(1,100,1):
	z=root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	f.write(z.getchildren()[0].text)
	f.write('\n')
	f.write(z.getchildren()[1].text)
	f.write('\n')

f.close()

