str = '1sdfg 2fjfhj 3hjghkfhrt 4fjdjdthf  5cgxfh, 6khkjh,7ter'
sep = ['  ']
def words(s):
    ind = [-1] + [i for i, x in enumerate(str) if x in sep] + [len(str)]
    print ind
    s = [[ind[i-1]+1, ind[i]] for i in range(len(ind)) if i != 0]
    print s
    return [str[a:b] for a,b in s if a != b]

print words(str)

def words2(str, sep):
    ind = (i for i, x in enumerate(str) if x in sep)
    a = 0
    for i in ind:
        yield str[a:i]
        a = i+1
    yield str[a:]

wrd = []
for i in words2(str, ['  ']):
    if i != '': wrd.append(i)
print wrd
print 1
print 2





'''
mylist = [x*x for x in range(3)]
for i in mylist :
    print(i)
print mylist, '*******************'


mygenerator = (x*x for x in range(3))
for i in mygenerator :
    print(i)
print mygenerator, '**********************'


def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i
        
mygenerator = createGenerator() # ??????? ?????????
print(mygenerator) # mygenerator ???????? ????????!
for i in mygenerator:
    print(i)
    
    
for i in mygenerator:
    print(i)
    

print mygenerator

l = [1, 2, 3, 4, 5]
a = list(x*x for x in l)
print a
'''
# end
