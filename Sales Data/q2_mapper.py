#!/usr/bin/python

import sys

#Write a Map Reduce program to find the monetary value of the highest individual sale for each seperate store (Reno, Toledo, Chandler).

store_dict = { "RENO" : 0.00,
	       "TOLEDO" : 0.00,
	       "CHANDLER" : 0.00}	

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	if store.upper() in store_dict and float(cost) > store_dict[store.upper()]:
	    store_dict[store.upper()] = float(cost)

for k, v in store_dict.items():
    print"{0}\t{1}".format(k, v)






