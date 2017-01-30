#!/usr/bin/python

import sys

prev_key = None
total_sales = 0
count = 0

#Write a Map Reduce program that calculates the mean (average) sales for each week-day

#We are using the datetime module to determine the day of the week by using the date.
#the value returned by the .weekday() function is between 0 - 6 with 0 being Monday and 6 being Sunday
#the python documentation can be found at http://docs.python.org/2/library/datetime.html#datetime.date.weekday

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    currnt_key, value = data_mapped

    if prev_key and prev_key != currnt_key:
        print "{0}\t{1}".format(prev_key, (total_sales/count))
	prev_key = currnt_key
	total_sales = float(value)
	count = 1

    prev_key = currnt_key
    total_sales += float(value)
    count += 1

print "{0}\t{1}".format(currnt_key, (total_sales/count))
	

