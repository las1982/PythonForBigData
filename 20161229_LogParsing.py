# run this command in cmd
# type net-dump.log | python 20161229_LogParsing.py
import sys
# data = sys.stdin.readlines()
# print "Counted", len(data), "lines."

# for line in sys.stdin:
#     print line

def words(s, sep):
    ind = (i for i, x in enumerate(s) if x in sep)
    start = 0
    w = []
    for i in ind:
        w.append(s[start:i])
        start = i + 1
    w.append(s[start:])
    return w

time = []
sourceIP = []
targetIP = []
f = open('net-dump.log', 'r')
for ln in f:
    if '[S' in ln:
        w = words(ln, [' ', '.', ':'])
        time.append(w[0] + ':' + w[1] + ':' + w[2] + '.' + w[3])
        sourceIP.append(w[5] + '.' + w[6] + '.' + w[7] + '.' + w[8])
        targetIP.append(w[11] + '.' + w[12] + '.' + w[13] + '.' + w[14])
        # print [words(ln, [' ', '.', ':'])[i] for i in [0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14]]
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
