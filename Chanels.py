# -*- coding: utf-8 -*-

df = []
with open('ChanelsIN.txt') as f:
    for ln in f:
        row = []
        start = 0
        end = 0
        while True:
            end = ln.find('	', start)
            if end == -1: break
            row.append(ln[start:end])
            start = end + 1
        df.append(row)

start = i = 1
while True:
    if df[i][0] == df[start][0]:
        df[i].append(df[start][2].replace('Частота вещания: ', ''))
        df[i].append(df[start+1][2].replace('Поляризация: ', ''))
        df[i].append(df[start+2][2].replace('Модуляция: ', ''))
        df[i].append(df[start+3][2].replace('FEC: ', ''))
        df[i].append(df[start+4][2].replace('Символьная скорость (SR): ', ''))
        i += 1
        if i == df.__len__(): break
    else:
        start = i

out = open('ChanelsOUT.txt', 'a')
for i in df:
    str = ''
    i.pop(2)
    for j in i:
        str = str + j + '\t'
    str = str + '\n'
    out.write(str)
out.close()