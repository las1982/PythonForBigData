import pandas as pd


a = pd.read_csv('cs1.csv')
b = pd.read_csv('cs2.csv')

print a.ix[:, 4:]

a = [
     ('fdgfsdg', 'sdgjsrg', 'hsd', 'rgrse', 'h', 'gs', 'hsd', 'hw', 'er', 'ges', 'g', 'hrs')
    ,('fdgfsdg', 'wewe', 'hsd', 'hgsd', 'h', 'gs', 'hsd', 'hw', 'er', 'ges', 'g', 'hrs')
]
b = [
     ('fdgfsdg', 'sdgjsrg', 'hsd', 'rgrse', 'h', 'gs', 'hsd', 'hw', 'er', 'ges', 'g', 'hrs')
    ,('fdgfsdg', 'wewe', 'hsd', 'hgsd', 'h', 'gs', 'hsd', 'hw', 'er', 'ges', 'g', 'hrs')
    ,('fdgfsdg', 'fdshgs', 'hsd', 'rgrse', 'h', 'gs', 'hsd', 'hw', 'er', 'ges', 'g', 'hrs')
    ,('fdgfsdg', 'wewe', 'hsd', 'erhth', 'h', 'gs', 'hsd', 'hw', 'er', 'ges', 'g', 'hrs')
]

a = set(a)
b = set(b)
# print (a != b).any(1)
print (a - b) | (b - a)
print b ^ a
# https://docs.python.org/2/library/sets.html