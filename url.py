#!/usr/bin/python
import urllib
import re

link = "http://www.yahoo.com"
f = urllib.urlopen(link)
myfile = f.read()
print myfile
def cleanhtml(myfile):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def remove_tags(cleantext):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())
