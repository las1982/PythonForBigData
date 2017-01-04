def words(str, sep):
	ind = (i for i, x in enumerate(str) if x == sep)
	a = 0
	for i in ind:
		yield str[a:i]
		a = i+1
	yield str[a:]

	
for i in words('h hhdshd jfd jfd jr j fd jd fjfd jf djfdj ', ' '):
	print i
	

with open("net-dump.log", 'r') as f:
	file = open("net-dump(filtered).log", "w")
	for line in f:
		if 'Flags [S]' in line:
			cnt = 0
			for w in words(line, ' '):
				if cnt in [0, 2, 4]:
					file.write(w + ' ')
				cnt += 1
			file.write('\n')
	file.close()


