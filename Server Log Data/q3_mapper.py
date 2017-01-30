#!/usr/bin/python
import sys
import re
from urlparse import urlparse

#Write a Map Reduce program to find the most popular file - that is the file whose path occurs most often in the data. 
#IMPORTANT: some pathnames begin with "http://www.the-associates.co.uk". Please remove the portion so that all occurences of a file are counted.
#We are using urlprase - a built in python function to seperate the pathnames.

path_dict = {}
p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

for line in sys.stdin:
    data = line.strip()
    try:
        result = p.match(data)
        host, ignore, user, date, request, status, size = result.groups()
	url = request.split(" ")[1]
	docname = urlparse(url)
	path_dict[docname.path] = path_dict.get(docname.path, 0) + 1
    except: continue

for k, v in path_dict.items():
	print "{0}\t{1}".format(k,v)

