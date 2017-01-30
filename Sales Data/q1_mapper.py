#!/usr/bin/python

#Write a Map Reduce program to breakdown the sales by product category (Toys, Consumer Electronics) across all stores

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	if "TOY" in item.upper(): print"{0}\t{1}".format(item.upper(), cost)
	if "ELECTRONIC" in item.upper(): print"{0}\t{1}".format(item.upper(), cost)
