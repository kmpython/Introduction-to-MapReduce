#!/usr/bin/python

import sys

#Write a Map Reduce program to determine the number of hits to the site made by each different ip address.

count = 0

for line in sys.stdin:
	page_data = line.strip().split("\t")
	if len(page_data) != 2: 
		continue
	count += 1
	
print page_data[0], "\t", count	
		
