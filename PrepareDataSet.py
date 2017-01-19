f = open('test.txt', 'r')
dataFrame = []
for ln in f:
	l = ln.strip().split('	')
	dataFrame.append(l)
f.close()

dataFrame1 = []
for lst in dataFrame:
	r = []
	r.append(lst[0])
	row = ""
	L1 = ("'/" + lst[1])
	L2 = ("/" + lst[2]) if lst[2] != '0' else ""
	L3 = ("/" + lst[3]) if lst[3] != '0' else ""
	L4 = ("/" + lst[4]) if lst[4] != '0' else ""
	L5 = ("/" + lst[5]) if lst[5] != '0' else ""
	row = L1 + L2 + L3 + L4 + L5 + "/'"
	r.append(row)
	dates = []
	dates1 = []
	a = 1
	for i in lst[6:]:
		if i != '-':
			dates1.append(i)
		if i == '-' or a == len(lst[6:]):
			if len(dates1) != 0:
				dates.append([dates1[0], dates1[-1]])
			dates1 = []
		a = a + 1
	for d in dates:
		dataFrame1.append(r + d)

f = open('test1.txt', 'w')
for i in dataFrame1:
	f.write('(' + i[0] + ', ' + i[1] + ', ' + i[2] + ', ' + i[3] + ', ' + str(1 if i[3] == "'99990101'" else 0) + ', ' + "'<Attributes/>'),\n")
f.close()
