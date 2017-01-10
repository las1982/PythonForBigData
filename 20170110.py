#! /bin/env/ python
# run this command in cmd
# cd "C:\Users\Sasha\Documents\PythonStudy"
# type net-dump.log | python 20170103_LogParsing_by_teacher.py
# type -n 100 net-dump.log | python 20161229_LogParsing.py - first n rows
import sys

def words2(st, sep=' '):
    cPos = 0
    try:
        while True:
            sPos = st.index(sep, cPos+1)
            yield st[cPos:sPos]
            cPos = sPos + 1
        yield st[cPos:]
    except:
        1==1

f = open('net-dump.log', 'r')
dataFrame = []
for ln in f:
    record = []
    for w in words2(ln, sep=' '):
        record.append(w)
    dataFrame.append(record)
f.close()

dataFrame = filter(lambda x: x[1]=='IP', dataFrame)


def min_ip_map(record):
    i = 0
    sMin = ''
    sIP = ''
    for x in words2(record[0], ':'):
        if i == 1:
            sMin = x
            break
        i += 1
    i = 0
    for x in words2(record[2], '.'):
        if i == 4:break
        sIP = sIP + x + '.'
        i += 1
    return (sMin, sIP)
print map(min_ip_map, dataFrame)