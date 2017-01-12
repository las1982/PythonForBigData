# raw_input('jljl')

f = open('testRW.txt', 'a+')
a = []
for i in range(10):
    i = str(i)
    f.write(i + '\n')
    a.append(i)
f.writelines(a)
f.close()