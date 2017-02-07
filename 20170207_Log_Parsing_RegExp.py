# run this command in cmd
# type net-dump.log | python 20161229_LogParsing.py
import sys
# data = sys.stdin.readlines()
# print "Counted", len(data), "lines."

# for line in sys.stdin:
#     print line
import re

x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2(5[0-5]|[0-4]\d))'
IpRegExp = "(" + x + "\.){3}" + x

time = []
sourceIP = []
targetIP = []
f = open('net-dump.log', 'r')
flagS = '\[.*S.*\]'
for ln in f:
    if len(list(re.finditer(flagS, ln))) != 0:
        IPs = re.finditer(IpRegExp, ln)
        sourceIP.append(IPs.next().group())
        targetIP.append(IPs.next().group())
f.close()
sourceIPunic = set(sourceIP)
targetIPunic = set(targetIP)

n = 0
l = []
for sIPunic in sourceIPunic:
    for IP in targetIP:
        if sIPunic == IP:
            n += 1
    # l.append(sIPunic + ' - ' + IP + ' - ' + str(n))
    print sIPunic + ' - ' + IP + ' - ' + str(n)
    n = 0
