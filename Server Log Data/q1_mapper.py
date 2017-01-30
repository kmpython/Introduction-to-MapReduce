#!/usr/bin/python
import sys
import re

#Write a Map Reduce problem which will display the number of hits for each different file on the website. 
#using regex to parse the input data
p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

ip_dict = {}
	
for line in sys.stdin:
    data = line.strip()
    data_list = []
    try:
        result = p.match(data)
        host, ignore, user, date, request, status, size = result.groups()
    except: continue

    ip_dict[host] = ip_dict.get(host, 0) + 1

#printing out all the unique ip host and the count of their occurences
for k, v in ip_dict.items():
    print "{0}\t{1}".format(k, v)
