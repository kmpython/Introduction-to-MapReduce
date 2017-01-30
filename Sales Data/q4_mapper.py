#!/usr/bin/python

import sys
from datetime import datetime

#Write a Map Reduce program that calculates the mean (average) sales for each week-day

#We are using the datetime module to determine the day of the week by using the date.
#the value returned by the .weekday() function is between 0 - 6 with 0 being Monday and 6 being Sunday
#the python documentation can be found at http://docs.python.org/2/library/datetime.html#datetime.date.weekday

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
	print "{0}\t{1}".format(weekday, cost)

