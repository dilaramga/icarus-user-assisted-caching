#Value of every parameter i.e. latency, link load, cache hit ratio, path streatch has increased by a bit
import csv

with open("test1_rec_icn.txt") as text_file:
    for row in text_file:
        if len(row)<=50:
            print row
