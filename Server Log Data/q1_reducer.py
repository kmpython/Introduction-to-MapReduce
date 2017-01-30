#!/usr/bin/python

import sys

#Write a Map Reduce problem which will display the number of hits for each different file on the website. 

prev_ip_addr = None
total_count = 0
hit_count = 0

for line in sys.stdin:
	log_data = line.strip().split("\t")
	if len(log_data) != 2: continue
	
	ip_addr, hit_count = log_data
	
	if prev_ip_addr is None:
		prev_ip_addr = ip_addr
		total_count = hit_count
	elif prev_ip_addr == ip_addr:
		total_count = total_count + hit_count
	elif prev_ip_addr != ip_addr:
		print prev_ip_addr, "\t", total_count
		total_count = hit_count
		prev_ip_addr = ip_addr

print ip_addr, "\t", total_count	
		
