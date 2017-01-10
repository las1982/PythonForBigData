#! /bin/env python

import sys

def my_split(st, sep=' '):
    cPos = 0
    try:
        while True:
            sPos = st.index(sep, cPos+1)
            yield st[cPos:sPos]
            cPos = sPos+1
    except:
        yield st[cPos:]

# Create a list of lists for future processing
dataFrame = []

# Read line from stdin
#for line in sys.stdin:
f = open('net-dump.log', 'r')
for line in f:
    record = []
    # Split line
    for word in my_split(line):
        record.append(word)
    dataFrame.append(record)
f.close()

# Remove any records, which is not 'IP'
dataFrame = filter(lambda x: x[1]=='IP', dataFrame)


def min_ip_map(record):
    sMin = [x for x in my_split(record[0], ':')][1]
    sIpPort = [x for x in my_split(record[2], '.')]
    sIP = sIpPort[0]+'.'+sIpPort[1]+'.'+sIpPort[2]+'.'+sIpPort[3]
    return (sMin, sIP)

mapData = map(min_ip_map, dataFrame)

print mapData

d = {}


for sMin, sIP in mapData:
    if d.has_key(sMin) :
        d[sMin].add(sIP)
    else:
        d[sMin] = set([sIP])

print d
