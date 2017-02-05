# -*- coding: utf-8 -*-

out = open('ChanelsOUT.txt', 'w')

df = []

with open('ChanelsIN.txt') as f:
    for ln in f:
        row = []
        start = 0
        end = 0
        while True:
            end = ln.find('	', start)
            if end == -1: break
            row.append(ln[start:end].decode('utf-8').encode('utf-8'))
            start = end + 1
        print row
out.close()