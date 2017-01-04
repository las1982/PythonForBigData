str = '1sdfg 2fjfhj 3hjghkfhrt 4fjdjdthf 5cgxfh, 6khkjh,7ter'
sep = ' '
def words1(s):
    ind = [-1] + [i for i, x in enumerate(str) if x == sep] + [len(str)-1]
    s = [[ind[i-1]+1, ind[i]] for i in range(len(ind)) if i != 0]
    return [str[a:b] for a,b in s if a != b]
print 111
print words1(str)

def words2(s):
    words = []
    strt = 0
    while True:
        try:
            pos = s.index(sep, strt)
        except:
            break
        words.append(s[strt:pos])
        strt = pos + 1
    words.append(s[pos:])
    return words
print 222
print words2(str)

def words3(s, sep):
    ind = (i for i, x in enumerate(s) if x == sep)
    start = 0
    for i in ind:
        yield s[start:i]
        start = i + 1
    yield s[start:]

for w in words3(str, ' '):
    print w